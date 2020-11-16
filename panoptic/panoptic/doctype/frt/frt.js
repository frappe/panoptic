// Copyright (c) 2020, Internet Freedom Foundation and contributors
// For license information, please see license.txt

frappe.ui.form.on('FRT', {
	refresh: function (frm) {
		if (frm.doc.state) {
			frm.set_query("district", function () {
				return {
					filters: {
						state: frm.doc.state,
					}
				}
			});
		}

		frm.set_query("parent_frt", function () {
			return {
				filters: {
					is_group: 1,
				}
			}
		});
	},

	state: function (frm) {
		frm.set_query("district", function () {
			return {
				filters: {
					state: frm.doc.state,
				}
			}
		});
	}

});
