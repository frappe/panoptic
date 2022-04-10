# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.website.website_generator import WebsiteGenerator

class RTI(WebsiteGenerator):
	def autoname(self):
		if not self.name:
				self.name = make_autoname("RTI-.#####")

	def make_route(self):
		return 'right-to-information/' + self.name

	def on_update(self):
		if self.status == "Draft":
			self.published = 0
		else:
			self.published = 1

	def get_context(self, context):
		context.metatags = {
			"name": "RTI: {0}".format(self.title),
			"description": "RTI filed to {0}".format(self.authority),
			"image": "/assets/panoptic/images/meta/rti.png",
			"og:type": "article"
		}
		context.frts = self.get_linked_frts()

	def get_linked_frts(self):
		all_frts = []
		frts = frappe.get_all("FRT RTI", fields=["parent"], filters={'rti': self.name}, pluck="parent", distinct=True)
		for frt in frts:
			frt_doc = frappe.get_doc("FRT", frt)
			if frt_doc.published:
				all_frts.append(frt_doc)

		return all_frts