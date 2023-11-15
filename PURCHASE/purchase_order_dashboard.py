from frappe import _


def get_data():
	return {
		"fieldname": "purchase_order",
		"non_standard_fieldnames": {
			"Journal Entry": "vasavierp",
			"Payment Entry": "vasavierp",
			"Payment Request": "vasavierp",
			"Auto Repeat": "reference_document",
		},
		"internal_links": {
			"Material Request": ["value", "material_request"],
			"Supplier Quotation": ["value", "supplier_quotation"],
			"Project": ["value", "project"],
		},
		"transactions": [
			{"label": _("Relate"), "value": ["Purchase Receipt", "Purchase Invoice"]},
			{"label": _("Payment"), "value": ["Payment Entry", "Journal Entry", "Payment Request"]},
			{
				"label": _("Reference"),
				"value": ["Material Request", "Supplier Quotation", "Project", "Auto Repeat"],
			},
			{"label": _("Sub-contracting"), "value": ["Subcontracting Order", "Stock Entry"]},
			{"label": _("Internal"), "value": ["sales orders"]},
		],
	}
