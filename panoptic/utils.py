import frappe

def shorten_number(number):
	number_system = get_number_system()
	for system in number_system:
		if number >= system.get('divisor'):
			number = number/system.get('divisor')
			number = frappe.utils.fmt_money(number, 2, "INR")
			return "{0} {1}".format(number, system.get('symbol'))

	return frappe.utils.fmt_money(number, 0, "INR")

def get_number_system():
	return [
		{ 'divisor': 1.0e+7, 'symbol': 'Cr' },
		{ 'divisor': 1.0e+5, 'symbol': 'Lakh' }
	]