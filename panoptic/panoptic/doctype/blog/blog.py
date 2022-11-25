# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from panoptic.panoptic.search import update_index_for_doc, remove_document_from_index

class Blog(WebsiteGenerator):
	def make_route(self):
		return 'case-study/' + self.scrub(self.title)

	def get_context(self, context):
		meta_image = "/assets/panoptic/images/meta/column.png"

		if self.category == "Update":
			meta_image = "/assets/panoptic/images/meta/updates.png"
		if self.category == "Case Study":
			meta_image = "/assets/panoptic/images/meta/case-study.png"

		context.metatags = {
			"name": "Case Study: {0}".format(self.title),
			"description": self.description or "Literature and reports about facial recognition tech in India",
			"image": self.meta_image or meta_image,
			"og:type": "article"
		}

	def on_update(self):
		if self.published:
			update_index_for_doc(self.doctype, self.name)
		else:
			remove_document_from_index(self.doctype, self.name)
		return super().on_update()

	def on_trash(self):
		remove_document_from_index(self.doctype, self.name)
		return super().on_trash()

	def get_search_doc(self):
		return frappe._dict(
			name=f"{self.doctype}////{self.name}",
			title=self.title,
			type=self.category,
			content=self.content,
			path=self.route,
			keywords="",
		)
