# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

from panoptic.panoptic.api import get_state_route_map, get_state_wise_frt
from panoptic.utils import shorten_number

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
		context.cities = self.get_all_cities(filters={ "state": self.name })

		if self.name == "Central":
			context.is_central = True
			context.section_title = "Central Level FRT Systems"
			context.frt_list_title = "List of Central FRTs"
			context.button_label = None
			context.button_id = None
		else:
			context.is_central = False
			context.section_title = "<span class='text-white'>FRT Systems in</span> {0}".format(self.state_name)
			context.frt_list_title = "List of FRTS installed in the state"
			context.button_label = "View States List"
			context.button_id = "view-states-list"

		context.total_frt = frappe.db.count("FRT", {"state": self.name, 'published': 1}) or 0
		context.total_frt_in_use = frappe.db.count("FRT", {"state": self.name, 'published': 1, "status": "In Utilization"}) or 0
		context.total_cost = shorten_number(sum(frappe.db.get_all("FRT", fields=["amount_spent"], filters={ "state": self.name, 'published': 1 }, pluck="amount_spent")))

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
			fields = ["name", "authority", "district_name", "purpose", "route", "status"]

		filters.update({
			"published": 1
		})

		return frappe.get_all("FRT", fields=fields, filters=filters, limit=30)

	def get_all_cities(self, filters={}, fields=None):
		if not fields:
			fields = ['route', 'title', 'subtitle', 'published_by', 'published_date', 'description', 'cover_image', 'for_city']

		filters.update({
			"published": 1
		})


		return frappe.db.get_all("City", fields=fields, filters=filters, order_by="published_date desc")