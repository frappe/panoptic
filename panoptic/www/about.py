import frappe

def get_context(context):
	context.no_cache = 1
	context.about = frappe.get_doc("About Page")
	context.team = frappe.get_all("Team Member", filters={"show_on_website": 1}, fields=["*"], order_by="website_order")