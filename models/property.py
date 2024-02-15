from odoo import fields, models


class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Name", required=True)
    type_id = fields.Many2one('estate.property.type',String="Property Type")
    tag_ids = fields.Many2many('estate.property.tag', String="Property Tag")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(String="Date")
    expected_price = fields.Float(String="Expected Price")
    best_offer = fields.Float(String="best offer")
    selling_price = fields.Float(String="Selling price")

    offer_ids = fields.One2many('estate.property.form', 'property_id', String="Offers")

    description = fields.Text(string="Description")
    bedrooms = fields.Integer(String="Bedrooms")
    living_area = fields.Integer(String="living rooms")
    facades = fields.Integer(String="facades")
    garage = fields.Boolean(String="garage", default=False)
    garden = fields.Boolean(String="garden", default=False)
    garden_area = fields.Integer(String="garden area")
    Garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('West', 'west'), ('East', 'east')],
        String="Garden orientation", default="north")


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(string="Name", required=True)

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(string="Name", required=True)
