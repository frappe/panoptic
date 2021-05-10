# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class Blog(WebsiteGenerator):
	def make_route(self):
		return 'case-study/' + self.scrub(self.title)

	def get_context(self, context):
		meta_image = "/assets/panoptic/images/meta/column.png"

		if self.category == "Update":
			meta_image = "/assets/panoptic/images/meta/updates.png"
		if self.category == "Case Study":
			meta_image = "/assets/panoptic/images/meta/case-study.png"

		context.metatags = {
			"name": "Case Study: {0}".format(self.title),
			"description": self.description or "Literature and reports about facial recognition tech in India",
			"image": self.meta_image or meta_image,
			"og:type": "article"
		}
