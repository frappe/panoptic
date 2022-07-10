from __future__ import unicode_literals
import frappe


def execute():
	# patch to update route field
	frappe.reload_doctype('RTI')
	
	for rti in frappe.get_all("RTI", fields=["name", "status"], filters={"published": 1}):
		rti_doc = frappe.get_doc("RTI", rti.name)
		print(rti_doc.name, rti.status)
		rti_doc.on_update()
