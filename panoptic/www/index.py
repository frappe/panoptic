import frappe

def get_context(context):
	context.total_frt = frappe.db.count("FRT")
	context.total_frs = frappe.db.count("Facial Recognition System")
	context.state_wise_frt = get_state_wise_frt()
	context.state_routes = get_state_route_map()
	context.total_authorities = frappe.db.count("Authority")

def get_state_route_map():
	states = frappe.get_all("State", fields={"state_id", "route"})
	return {d.state_id:d.route for d in states}

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