from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property', 'property_type_id')

    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', 'Type must be unique.')
    ]
    