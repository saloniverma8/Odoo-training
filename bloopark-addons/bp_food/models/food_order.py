import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date

from odoo import models, fields, api


class FoodOrder(models.Model):
    _name = "food.order"
    _description = "Order"

    # table = fields.One2many('food.tables', 'table', required=True, index=True)
    table = fields.Many2one('food.tables', 'Choose Table')
    name = fields.Char(string='Order', copy=False,
                       readonly=True, index=True,
                       default=lambda self: 'New')
    capacity = fields.Integer("Capacity")
    order_date = fields.Date(string='Order Date', required=True)
    # current_date = fields.Datetime(string='Current Date and Time')
    order_customer = fields.Many2one('res.partner', string='Name of Customer')
    order_dish = fields.Many2many('food.menu', string='Dish to be Ordered')
    order_server = fields.Many2one('hr.employee', string='Server/Waiter Name')
    order_amount = fields.Integer(string='Bill Total')
    # order_amount = fields.Float(string='Bill Total', compute='_bill_total', readonly=True)
    order_comments = fields.Char('Add comments here for customisation or Allergies')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'food.order.sequence') or 'New'
        result = super(FoodOrder, self).create(vals)
        return result

    def _bill_total(self):
        """
             To calculate the sum of the order
        """
        # for line in self.order_dish:
        print(f"XXXXXX: {self.dish_price}")
        # print(f"XXXXXX: {self.order_dish.dish_price}")
        order_amount = 1 # sum(self.order_dish.dish_price)
        return order_amount
