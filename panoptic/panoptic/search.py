import frappe
from frappe.search.full_text_search import FullTextSearch
from frappe.utils import strip_html_tags
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import ID, KEYWORD, TEXT, Schema
from whoosh.qparser import FieldsPlugin, MultifieldParser, WildcardPlugin
from whoosh.query import Prefix

from collections import defaultdict

INDEX_NAME = "panoptic"


class PanopticSearch(FullTextSearch):
	"""Wrapper for WebsiteSearch"""

	def get_schema(self):
		return Schema(
			title=TEXT(stored=True, field_boost=1.5),
			name=ID(stored=True),
			type=TEXT(stored=True),
			path=TEXT(stored=True),
			content=TEXT(stored=True, analyzer=StemmingAnalyzer()),
			keywords=KEYWORD(stored=True, scorable=True, commas=True, analyzer=StemmingAnalyzer()),
		)

	def get_id(self):
		return "name"

	def get_items_to_index(self):
		"""Get all routes to be indexed, this includes the static pages
		in www/ and routes from published documents

		Returns:
		        self (object): FullTextSearch Instance
		"""
		frts = self.get_docs("FRT", self.get_all_frts())
		blogs = self.get_docs("Blog", self.get_all_blogs())
		rtis = self.get_docs("RTI", self.get_all_rtis())
		cities = self.get_docs("City", self.get_all_cities())

		return frts + blogs + rtis + cities

	def get_all_frts(self):
		return frappe.get_all("FRT", filters={ "published": 1 }, pluck="name")

	def get_all_blogs(self):
		return frappe.get_all("Blog", filters={ "published": 1 }, pluck="name")
	
	def get_all_rtis(self):
		return frappe.get_all("RTI", filters=[["status", "!=", "Draft"]], pluck="name")
	
	def get_all_cities(self):
		return frappe.get_all("City", filters={ "published": 1 }, pluck="name")

	def get_docs(self, doctype, doc_list):
		documents = []
		for docname in doc_list:
			doc = frappe.get_doc(doctype, docname)
			documents.append(doc.get_search_doc())
		return documents

	def get_document_to_index(self, item):
		try:
			[doctype, name] = item.split("////")
			item = frappe.get_doc(doctype, name)
			return item.get_search_doc()
		except Exception:
			pass

	def search(self, text, scope=None, limit=20):
		"""Search from the current index

		Args:
		        text (str): String to search for
		        scope (str, optional): Scope to limit the search. Defaults to None.
		        limit (int, optional): Limit number of search results. Defaults to 20.

		Returns:
		        [List(_dict)]: Search results
		"""
		ix = self.get_index()

		results = None
		out = defaultdict(list)

		with ix.searcher() as searcher:
			parser = MultifieldParser(["title", "content", "keywords"], ix.schema)
			parser.remove_plugin_class(FieldsPlugin)
			parser.remove_plugin_class(WildcardPlugin)
			query = parser.parse(text)

			filter_scoped = None
			if scope:
				filter_scoped = Prefix(self.id, scope)
			results = searcher.search(query, limit=limit, filter=filter_scoped)

			for r in results:
				result = self.parse_result(r)
				out[result.type].append(result)

		return out

	def parse_result(self, result):
		title_highlights = result.highlights("title")
		content_highlights = result.highlights("content")
		keyword_highlights = result.highlights("keywords")

		return frappe._dict(
			title=result["title"],
			path=result["path"],
			type=result["type"],
			keywords=result["keywords"],
			title_highlights=title_highlights,
			content_highlights=content_highlights,
			keyword_highlights=keyword_highlights,
		)



def update_index_for_doc(doctype, docname):
	search = PanopticSearch(INDEX_NAME)
	return search.update_index_by_name(f"{doctype}////{docname}")

def remove_document_from_index(doctype, docname):
	search = PanopticSearch(INDEX_NAME)
	return search.remove_document_from_index(f"{doctype}////{docname}")

def build_index_for_all_routes():
	search = PanopticSearch(INDEX_NAME)
	return search.build()


@frappe.whitelist(allow_guest=True)
def search(query):
	ws = PanopticSearch(index_name=INDEX_NAME)
	return ws.search(query)