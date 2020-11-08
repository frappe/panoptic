# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

from panoptic.panoptic.api import get_state_route_map, get_state_wise_frt

class State(WebsiteGenerator):

	published = 1
	website = frappe._dict(
		page_title_field="state_name",
		no_cache=1,
		sitemap=1
	)

	def autoname(self):
		self.name = self.state_name

	def get_context(self, context):
		context.no_cache = 1
		context.frts = self.get_all_frts(filters={ "state": self.name })

		context.total_frt = frappe.db.count("FRT", {"state": self.name}) or 0
		context.total_frt_in_use = frappe.db.count("FRT", {"state": self.name, "status": "In Utilization"}) or 0
		context.total_cost = sum(frappe.db.get_all("FRT", fields=["amount_spent"], filters={ "state": self.name }, pluck="amount_spent"))

		context.state_wise_frt = get_state_wise_frt()
		context.state_name_routes = get_state_route_map(field="state_name")
		context.state_routes = get_state_route_map(field="state_id")

		context.metatags = {
			"name": "FRT Systems in {0}".format(self.state_name),
			"description": "Facial Recognition Systems in {0}".format(self.state_name),
			"image": "/assets/panoptic/images/meta/generic.png"
		}

	def get_all_frts(self, filters={}, fields=None):
		if not fields:
			fields = ["name", "authority", "district_name", "technology_provider", "route"]

		filters.update({
			"published": 1
		})

		return frappe.get_all("FRT", fields=fields, filters=filters, limit=30)