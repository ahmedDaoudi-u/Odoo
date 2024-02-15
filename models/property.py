from odoo import fields, models,api


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

    offer_ids = fields.One2many('estate.property.offer', 'property_id', String="Offers")

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

    sales_id = fields.Many2one('res.users', String="Salesman")
    buyer_id = fields.Many2one('res.partner', String="Buyer")

    @api.depends('living_area','garden_area')
    def _adding_space(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    total_area = fields.Integer(String="Total Area", compute="_adding_space")


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(string="Name", required=True)

class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char(string="Name", required=True)
