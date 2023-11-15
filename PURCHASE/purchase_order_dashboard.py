from frappe import _


def get_data():
	return {
		"fieldname": "purchase_order",
		"non_standard_fieldnames": {
			"Journal Entry": "reference_name",
			"Payment Entry": "reference_name",
			"Payment Request": "reference_name",
			"Auto Repeat": "reference_document",
		},
		"internal_links": {
			"Material Request": ["values", "material_request"],
			"Supplier Quotation": ["values", "supplier_quotation"],
			"Project": ["values", "project"],
		},
		"transactions": [
			{"label": _("Related"), "values": ["Purchase Receipt", "Purchase Invoice"]},
			{"label": _("Payment"), "values": ["Payment Entry", "Journal Entry", "Payment Request"]},
			{
				"label": _("Reference"),
				"values": ["Material Request", "Supplier Quotation", "Project", "Auto Repeat"],
			},
			{"label": _("Sub-contracting"), "values": ["Subcontracting Order", "Stock Entry"]},
			{"label": _("Internal"), "values": ["Sales Order"]},
		],
	}
