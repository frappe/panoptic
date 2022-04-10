from __future__ import unicode_literals
import frappe


def execute():
	# patch to update published field
	frappe.reload_doctype('RTI')
	
	for rti in frappe.get_all("RTI", fields=["name", "status"]):
		frappe.db.set_value("RTI", rti.get('name'), "published", int(rti.status != "Draft"))

	for state in frappe.get_all("State", pluck="name"):
		frappe.db.set_value("State", state, "published", 1)
	