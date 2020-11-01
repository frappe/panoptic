import frappe
from frappe.utils import cint

def get_context(context):
	context.no_cache = 1
	context.title = "Sign the Petition"
	context.submitted = False

	if cint(frappe.form_dict.thank_you):
		context.title = "Thank You"
		context.submitted = True

	if frappe.form_dict.full_name:
		frappe.form_dict["doctype"] = "Petition"
		doc = frappe.get_doc({
			"doctype": "Petition",
			"full_name": frappe.form_dict.full_name,
			"email": frappe.form_dict.email,
			"organization": frappe.form_dict.organization,
			"designation": frappe.form_dict.designation,
			"above_eighteen": frappe.form_dict.above_eighteen,
			"agree_terms": frappe.form_dict.agree_terms
		})
		doc.insert(ignore_permissions=True)
		frappe.local.flags.redirect_location = "/sign-the-petition?thank_you=1"
		raise frappe.Redirect
