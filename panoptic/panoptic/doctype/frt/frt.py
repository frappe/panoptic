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
		context.no_cache = 1
		fields = ["name", "authority", "district_name", "technology_provider", "route"]
		frts_in_district = frappe.get_all("FRT", fields=fields, filters={"district": self.district, "name": ['!=', self.name], "published": 1}, or_filters={"state": self.state}, limit=3)
		context.frts = frts_in_district
		context.news_links = False
		context.other_links = False
		context.case_studies = self.get_linked_case_studies()
		context.rti_list = self.get_all_rtis()

		context.child_frts = []
		context.parent = None

		if self.is_group:
			context.child_frts = frappe.get_all("FRT", filters={"published": 1, "parent_frt": self.name}, fields=['name', 'route', 'authority'])

		if self.parent_frt:
			context.parent = frappe.get_doc("FRT", self.parent_frt)

		for link in self.links:
			if link.type == "News Article":
				context.news_links = True
				break

		for link in self.links:
			if link.type != "News Article":
				context.other_links = True
				break

		context.state_route = frappe.get_value("State", self.state, 'route')

	def get_linked_case_studies(self):
		all_case_studies = []
		studies = frappe.get_all("Case Study FRT Link", fields=["parent"], filters={'frt': self.name}, pluck="parent")
		for study in studies:
			study_doc = frappe.get_doc("Blog", study)
			if study_doc.published and study_doc.category == "Case Study":
				all_case_studies.append(study_doc)

		return all_case_studies

	def get_all_rtis(self):
		all_rtis = []
		for rti in self.rti:
			if frappe.db.get_value('RTI', rti.rti, 'state') != "Draft":
				all_rtis.append(rti)

		return all_rtis

