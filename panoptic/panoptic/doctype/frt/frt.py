# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.website.website_generator import WebsiteGenerator

class FRT(WebsiteGenerator):
	def autoname(self):
		if not self.name:
				self.name = make_autoname("FRT-.######")

	def on_update(self):
		self.route = self.make_route()

	def make_route(self):
		return frappe.get_value("State", self.state, 'route') + '/' + self.name

	def get_context(self, context):
		fields = ["name", "authority", "district_name", "technology_provider", "route"]
		frts_in_district = frappe.get_all("FRT", fields=fields, filters={"district": self.district}, limit=3)
		frts_in_state = frappe.get_all("FRT", fields=fields, filters={"state": self.state}, limit=3)
		context.frts = frts_in_district + frts_in_state
		context.state_route = frappe.get_value("State", self.state, 'route')


