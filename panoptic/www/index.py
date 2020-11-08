import frappe

def get_context(context):
	context.total_frt = frappe.db.count("FRT")
	context.total_frs = frappe.db.count("Facial Recognition System")
	context.state_wise_frt = get_state_wise_frt()
	context.state_routes = get_state_route_map(field="state_id")
	context.state_name_routes = get_state_route_map(field="state_name")
	context.total_authorities = frappe.db.count("Authority")

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
			`frt`.`state`=`st`.`name` AND
			`frt`.`published` = 1
		GROUP BY
			`frt`.`state`
	""", as_dict=1)

	return {d.state_id:d.count for d in data}