import frappe

def get_context(context):
	context.no_cache = 1
	fields = ['route', 'title', 'published_by', 'published_date', 'description']
	context.case_studies = frappe.db.get_all("Case Study", fields=fields, filters={"published": 1}, order_by="published_date desc")