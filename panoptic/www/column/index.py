import frappe

def get_context(context):
	context.current_state = frappe.form_dict.state if frappe.form_dict.state != "All" else None
	context.current_category = frappe.form_dict.category if frappe.form_dict.category != "All" else None

	context.metatags = {
		"name": "Updates and Case Studies",
		"description": "Literature and reports about facial recognition tech in India",
		"image": "/assets/panoptic/images/meta/case-study.png"
	}

	context.no_cache = 1

	if context.current_state:
		frts = get_all_frts_in_state(context.current_state)
		filters.append(["Case Study FRT Link", "frt", "in", frts])
	if context.current_category:
		filters.append(["category", "=", context.current_category])
	
	context.articles = get_all_articles()
	context.states = get_all_states()

def get_all_articles():
	fields = ['route', 'title', 'published_by', 'published_date', 'description', 'category']
	filters = [["published", "=", 1]]

	articles = frappe.db.get_all("Blog", fields=fields, filters=filters, order_by="published_date desc")

	for article in articles:
		article.member_doc = frappe.get_doc("Team Member", article.published_by).as_dict()

	return articles


def get_all_states():
	all_states = set()
	studies = frappe.get_all("Case Study FRT Link", fields=["parent", "frt"])
	for study in studies:
		is_published = frappe.db.get_value("Blog", study['parent'], "published")
		if is_published:
			all_states.add(frappe.db.get_value("FRT", study['frt'], "state"))

	return list(all_states)

def get_all_frts_in_state(state):
	fields = ["name"]

	filters = {
		"published": 1,
		"state": state
	}

	return frappe.get_all("FRT", fields=fields, filters=filters, pluck="name")
