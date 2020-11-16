def shorten_number(number):
	number_system = get_number_system()
	for system in number_system:
		if number >= system.get('divisor'):
			return "₹ {0} {1}".format(round((number/system.get('divisor')), 2), system.get('symbol'))

	return round(number, 2);

def get_number_system():
	return [
		{ 'divisor': 1.0e+7, 'symbol': 'Cr' },
		{ 'divisor': 1.0e+5, 'symbol': 'Lakh' }
	]