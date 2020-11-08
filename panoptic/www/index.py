import frappe
from panoptic.panoptic.api import get_state_route_map, get_state_wise_frt

def get_context(context):
	context.total_frt = frappe.db.count("FRT", {"published": 1})
	context.total_frs = frappe.db.count("Facial Recognition System")
	context.state_wise_frt = get_state_wise_frt()
	context.state_routes = get_state_route_map(field="state_id")
	context.state_name_routes = get_state_route_map(field="state_name")
	context.total_cost = sum(frappe.db.get_all("FRT", fields=["amount_spent"], filters={ "published": 1 }, pluck="amount_spent"))