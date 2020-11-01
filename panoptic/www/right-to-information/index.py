import frappe

def get_context(context):
	context.metatags = {
		"name": "Right To Information",
		"description": "RTIs Filed by Internet Freedom Foundation seeking more information about FRT systems",
		"image": "/assets/panoptic/images/meta/rti.png"
	}

	context.no_cache = 1
	fields = ['route', 'title', 'authority', 'rti_filed_by', 'status', 'filed_on']
	context.rtis = frappe.db.get_all("RTI", fields=['*'], filters={ 'status': ["!=", "Draft"]}, order_by="filed_on desc")