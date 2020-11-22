import frappe

def update_website_context(context):
	context.settings = frappe.get_doc("Panoptic Settings")
	context.site_url = frappe.utils.get_host_name_from_request()

def get_state_route_map(field="state_id"):
	states = frappe.get_all("State", fields={field, "route"})
	return {d[field]:d.route for d in states}

def get_state_wise_frt():
	data = frappe.db.sql("""
		SELECT
			`st`.`state_id`,
			count(`frt`.`name`) as count
		FROM
			`tabFRT` as `frt`,
			`tabState` as `st`
		WHERE
			`frt`.`state`=`st`.`name`
		GROUP BY
			`frt`.`state`
	""", as_dict=1)

	return {d.state_id:d.count for d in data}