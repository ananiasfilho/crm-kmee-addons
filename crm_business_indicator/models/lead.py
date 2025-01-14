# business_indicator_lead/models/lead.py
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    business_indicator = fields.Many2one('res.partner', string="Business Indicator")
    employees_quantity = fields.Selection([
        ('less_than_5', 'Less than 5'),
        ('5_10', '5-10'),
        ('10_20', '10-20'),
        ('20_50', '20-50'),
        ('50_100', '50-100'),
        ('more_than_100', 'More than 100')
    ], string="Employees Quantity", default='', required=False)
    # Adicionar o campo Segmento como Many2one
    lead_temperature = fields.Selection([
        ('Frio', 'Frio'),
        ('Morno', 'Morno'),
        ('Quente', 'Quente')
    ], string="Temperature", default='', required=False)
    # Adicionar o campo Segmento como Many2one
