import frappe

def get_context(context):
	context.metatags = {
		"name": "Right To Information",
		"description": "RTIs Filed by Internet Freedom Foundation seeking more information about FRT systems",
		"image": "/assets/panoptic/images/meta/rti.png"
	}

	context.no_cache = 1
	context.rtis = get_all_rtis()

def get_all_rtis():
	fields = ['route', 'title', 'authority', 'rti_filed_by', 'status', 'filed_on']
	rtis = frappe.db.get_all("RTI", fields=['*'], filters={ 'status': ["!=", "Draft"]}, order_by="filed_on desc")

	for rti in rtis:
		rti.member_doc = frappe.get_doc("Team Member", rti.rti_filed_by)

	return rtis