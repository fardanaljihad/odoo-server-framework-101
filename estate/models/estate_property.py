from odoo import api, exceptions, fields, models
from odoo.tools import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string='Available From',
        default=fields.Date.add(fields.Date.today(), months=3), 
        copy=False
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')]
    )
    state = fields.Selection(
        string='Status',
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        default='new',
        copy=False,
        required=True
    )
    active = fields.Boolean(default=True)
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    salesperson_id = fields.Many2one('res.users', string='Salesman', index=True, default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, copy=False, default=lambda self: self.env.user.partner_id)
    tag_ids = fields.Many2many('estate.property.tag', string='Property Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Integer(compute='_compute_total')
    best_price = fields.Float(compute='_compute_best_price', string='Best Offer')

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if not self.garden:
            self.garden_area = None
            self.garden_orientation = None
            return
        
        self.garden_area = 10
        self.garden_orientation = 'north'

    def action_set_sold(self):
        for record in self:
            if record.state == 'cancelled':
                raise exceptions.UserError('Cancelled properties cannot be sold.')
            
            record.state = 'sold'

        return True
    
    def action_set_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError('Sold properties cannot be cancelled')
            
            record.state = 'cancelled'

        return True
    
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price must be stricly positive.'),
        ('check_selling_price', 'CHECK(selling_price > 0)',
         'The selling price must be positive.')
    ]

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if float_is_zero(record.selling_price, precision_rounding=0.01):
                continue

            min_selling_price = record.expected_price * 0.9
            if float_compare(record.selling_price, min_selling_price, precision_rounding=0.01) < 0:
                raise exceptions.ValidationError(
                    'The selling price cannot be lower than 90% of the expected price.'
                )
