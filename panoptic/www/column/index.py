import frappe

def get_context(context):
	context.metatags = {
		"name": "Updates and Case Studies",
		"description": "Literature and reports about facial recognition tech in India",
		"image": "/assets/panoptic/images/meta/case-study.png"
	}

	context.no_cache = 1
	fields = ['route', 'title', 'published_by', 'published_date', 'description', 'category']
	context.case_studies = frappe.db.get_all("Blog", fields=fields, filters={"published": 1}, order_by="published_date desc")