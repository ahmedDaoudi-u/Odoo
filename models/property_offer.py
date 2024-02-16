from odoo import fields, models,api
from datetime import timedelta
from odoo.exceptions import ValidationError



class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offers"

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        String="Status")

    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")

    deadline = fields.Date(String="Deadline", compute="_deadline_date" ,inverse="_reverse_deadline")
    validity = fields.Integer(String="Validity")

    creation_date = fields.Date(String="Create Date")


    @api.constrains('validity')
    def _constrained_field(self):
        for rec in self:
            if rec.deadline < rec.creation_date:
                raise ValidationError("Opps ! ,You can not make a deadline date in the past")


    @api.depends('creation_date', 'validity')
    def _deadline_date(self):
        for rec in self:
            if rec.validity and rec.creation_date:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _reverse_deadline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days