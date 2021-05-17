from odoo import fields, models


class Sale(models.Model):
    _inherit = 'sale.order'
    _description = 'food_sales'

    sale_id = fields.Many2one('food.order', string='Food Sales')
