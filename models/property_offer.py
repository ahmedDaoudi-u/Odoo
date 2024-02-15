from odoo import fields, models


class PropertyForm(models.Model):
    _name = "estate.property.form"
    _description = "Estate Property Form"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        String="Status")

    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")

