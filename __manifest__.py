{
    "name": "Real estate ads",
    "version": "1.0",
    "website": "https://www.ahmed.com",
    "author": "ahmed",
    "description": "Real estate module for the ads of the business, anyways this is just a test",
    "data": [
        'security/ir.model.access.csv',
        'views/Property_offer_view.xml',
        'views/property_view.xml',
        'views/Property_view_type.xml',
        'views/property_view_tag.xml',
        'views/menu_item.xml',
        'data/estate.property.type.csv',
        'reports/property_report.xml',
        'reports/report_template.xml',
        'data/email_template.xml'
    ],
    "category": "Sales",
    "depends": ['base',"mail"],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
