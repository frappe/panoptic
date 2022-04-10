from __future__ import unicode_literals
import frappe


def execute():
	# patch to update published field
	for rti in frappe.get_all("RTI", pluck="name"):
		doc = frappe.get_doc("RTI", rti)
		
		if doc.status != "Draft":
			doc.published = True
		else:
			doc.published = False

		doc.save()
	