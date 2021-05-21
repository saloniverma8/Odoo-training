import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date

from odoo import models, fields, api


class BPOrder(models.Model):
    _inherit = "lunch.product.category"
    _description = "Order"


    # order_no = fields.Char("Order #", default='/')

    order_no = fields.Char(string='Order', copy=False,
                               readonly=True, index=True,
                               default=lambda self: 'New')

    # @api.depends('dish_order_line')
    # def _compute_order_amount(self):
    #     for line in self:
    #         print(sum(line.dish_order_line.dish_price))
    #         line.order_amount = sum(line.dish_order_line.dish_price)

    # on create method
    # @api.model
    # def create(self, vals):
    #     obj = super(lunch.product.category, self).create(vals)
    #     if obj.order_no == '/':
    #         number = self.env['ir.sequence'].get('1') or '/'
    #         obj.write({'order_no': number})
    #     return obj

    @api.model
    def create(self, vals):
        if vals.get('order_no', 'New') == 'New':
            vals['order_no'] = self.env['ir.sequence'].next_by_code(
                'lunch.product.category.sequence') or 'New'
        result = super(BPOrder, self).create(vals)
        return result

    # # on button click event
    # @api.one
    # def submit_application(self):
    #     if self.order_no == '/':
    #         sequence_id = self.env['ir.sequence'].search([('code', '=', 'your.sequence.code')])
    #         sequence_pool = self.env['ir.sequence']
    #         application_no = sequence_pool.sudo().get_id(sequence_id.id)
    #         self.write({'order_no': order_no})
