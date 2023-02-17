import frappe

def get_context(context):
	context.metatags = {
		"name": "Panoptic Cities",
		"description": "A deep dive into facial recognition tech implemented by major cities in India",
		"image": "/assets/panoptic/images/meta/case-study.png"
	}

	context.no_cache = 1
	settings = frappe.get_doc("Panoptic Settings")
	if settings.enable_cities:
		context.cities = get_all_cities()
	else:
		context.city = []

def get_all_cities():
	fields = ['route', 'title', 'subtitle', 'published_by', 'published_date', 'description', 'cover_image']

	cities = frappe.db.get_all("City", fields=fields, filters=[["published", "=", 1]], order_by="published_date desc")

	for city in cities:
		city.member_doc = frappe.get_doc("Team Member", city.published_by).as_dict()

	return cities
