import frappe

def get_context(context):
	context.total_frt = frappe.db.count("FRT")
	context.total_frs = frappe.db.count("Facial Recognition System")
	context.total_authorities = frappe.db.count("Authority")