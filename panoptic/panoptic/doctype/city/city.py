# Copyright (c) 2022, Internet Freedom Foundation and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class City(WebsiteGenerator):
	def make_route(self):
		return 'cities/' + self.scrub(self.for_city)

	def get_context(self, context):
		context.metatags = {
			"name": "Panoptic: {0}".format(self.title),
			"description": self.description,
			"image": "/assets/panoptic/images/meta/cities.png",
			"og:type": "article"
		}
