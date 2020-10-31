import frappe

def get_context(context):
	context.no_cache = 1
	fields = ['route', 'title', 'authority', 'rti_filed_by', 'status', 'filed_on']
	context.rtis = frappe.db.get_all("RTI", fields=['*'], filters={ 'status': ["!=", "Draft"]}, order_by="filed_on desc")