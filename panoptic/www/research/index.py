import frappe

def get_context(context):
	context.metatags = {
		"name": "Research",
		"description": "Articles, documents and other resources we curate during the course of our research",
		"image": "/assets/panoptic/images/meta/generic.png"
	}

	context.no_cache = 1
	context.resources = get_all_resources()

def get_all_resources():
	fields = ['route', 'title', 'publisher', 'published_date', 'description']

	resources = frappe.db.get_all("Research", fields=fields, filters={ 'published': True}, order_by="creation desc")

	return resources