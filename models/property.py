from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(String="Date")
    expected_price = fields.Float(String="Expected Price")
    best_offer = fields.Float(String="best offer")
    selling_price = fields.Float(String="Selling price")
    bedrooms = fields.Integer(String="Bedrooms")
    living_area = fields.Integer(String="living rooms")
    facades = fields.Integer(String="facades")
    garage = fields.Boolean(String="garage", default=False)
    garden = fields.Boolean(String="garden", default=False)
    garden_area = fields.Integer(String="garden area")
    Garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('West', 'west'), ('East', 'east')],
        String="Garden orientation", default="north")


class property_type(models.Model):
    _name = "estate.property_type"

    name = fields.Char(string="Name", required=True)
