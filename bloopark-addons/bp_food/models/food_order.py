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
    dish_order_line = fields.Many2one('food.menu', string='Dish Order Line', ondelete='cascade', copy=False)
    order_dishprice = fields.Float(related='order_dish.dish_price')
    order_server = fields.Many2one('hr.employee', string='Server/Waiter Name')
    order_amount = fields.Integer(string='Bill Total')
    # order_amount = fields.Float(string='Bill Total', compute='_compute_total_price')
    quantity = fields.Float('Quantity', required=True, default=1)
    order_comments = fields.Char('Add comments here for customisation or Allergies')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'food.order.sequence') or 'New'
        result = super(FoodOrder, self).create(vals)
        return result

    @api.depends('dish_order_line.dish_price')
    def _bill_total(self):
        """
             To calculate the sum of the order
        """
        self.order_amount = 0
        for line in self:
            do = self.dish_order_line
            self.order_amount = self.order_amount + do.dish_price
        return self.order_amount

    @api.depends('order_dish', 'quantity')
    def _compute_total_price(self):
        for line in self:
            line.order_amount = line.quantity * line.order_dish.dish_price

# expected singleton error
                #                                  + sum(
                # (line.topping_ids_1 | line.topping_ids_2 | line.topping_ids_3).mapped('order_amount')))
