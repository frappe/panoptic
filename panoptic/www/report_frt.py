import frappe
from frappe.utils import cint

def get_context(context):
	context.metatags = {
		"name": "Report an FRT System",
		"description": "Help us keep facial recognition tech in check",
		"image": "/assets/panoptic/images/meta/report.png"
	}

	context.no_cache = 1
	context.title = "Report an FRT System"
	context.submitted = False

	if cint(frappe.form_dict.thank_you):
		context.title = "Thank You"
		context.submitted = True

	if frappe.form_dict.full_name:
		frappe.form_dict["doctype"] = "Petition"
		doc = frappe.get_doc({
			"doctype": "Report FRT",
			"full_name": frappe.form_dict.full_name,
			"email": frappe.form_dict.email,
			"location": frappe.form_dict.location,
			"authority": frappe.form_dict.authority,
			"description": frappe.form_dict.description,
			"agree_terms": frappe.form_dict.agree_terms
		})
		doc.insert(ignore_permissions=True)
		frappe.local.flags.redirect_location = "/report-frt?thank_you=1"
		raise frappe.Redirect
