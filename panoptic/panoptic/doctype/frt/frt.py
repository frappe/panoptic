# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class FRT(WebsiteGenerator):
	def on_update(self):
		self.route = self.make_route()

	def make_route(self):
		return frappe.get_value("State", self.state, 'route') + '/' + self.name

