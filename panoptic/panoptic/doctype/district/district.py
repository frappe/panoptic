# -*- coding: utf-8 -*-
# Copyright (c) 2020, Internet Freedom Foundation and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.utils import cstr
from frappe.model.naming import make_autoname
import frappe
from frappe.model.document import Document

class District(Document):
	def autoname(self):
		self.name = (cstr(self.district_name).strip() + ", " + cstr(self.state).strip())

		if frappe.db.exists("District", self.name):
			self.name = make_autoname(cstr(self.district_name).strip() + ", " + cstr(self.state).strip() + "-.#")
