from odoo import models, fields

class UtmSource(models.Model):
    _name = 'utm.source'
    _description = 'Marketing Source'

    name = fields.Char(string="Source Name", required=True)
    description = fields.Text(string="Description")
