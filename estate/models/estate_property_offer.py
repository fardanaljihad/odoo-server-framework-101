from odoo import api, exceptions, fields, models

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy=False
    )
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default=7, string='Validity (days)')
    # inverse method is called when saving the record, while the compute method is called at each change of its dependencies.
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline', string='Deadline')
    property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Date.today()
            record.date_deadline = fields.Date.add(create_date, days=record.validity)

    def _inverse_date_dateline(self):
        for record in self:
            diff = record.date_deadline - fields.Date.to_date(record.create_date)
            record.validity = diff.days

    def action_accept(self):
        for record in self:
            if record.property_id.state == 'sold':
                raise exceptions.UserError('Cannot accept an offer for a sold property.')
            
            record.status = 'accepted'
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price

        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'

        return True
    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)',
         'The offer price must be stricly positive.')
    ]
    