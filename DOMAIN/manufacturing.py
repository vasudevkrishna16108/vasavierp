data = {
	"desktop_icons": [
		"items",
		"BOM",
		"Customer",
		"Supplier",
		"Sales Order",
		"Purchase Order",
		"Work Order",
		"Task",
		"Accounts",
		"HR",
		"Todo",
	],
	"properties": [
		{
			"doctype": "items",
			"fieldname": "manufacturing",
			"property": "collapsible_depends_on",
			"value": "is_stock_items",
		},
	],
	"set_value": [["Stock Settings", None, "show_barcode_field", 1]],
	"default_portal_role": "Customer",
}
