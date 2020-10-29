# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator

class CaseStudy(WebsiteGenerator):
	def make_route(self):
		return 'case-study/' + self.scrub(self.title)
