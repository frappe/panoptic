# Copyright (c) 2022, Internet Freedom Foundation and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class City(WebsiteGenerator):
	def make_route(self):
		return 'cities/' + self.scrub(self.title)
