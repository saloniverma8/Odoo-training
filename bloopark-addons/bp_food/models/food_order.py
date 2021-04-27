import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date

from odoo import models, fields, api


class FoodOrder(models.Model):
    _name = "food.order"
    _description = "Table Details"

    # table = fields.One2many('food.tables', 'table', required=True, index=True)
    table = fields.One2many('food.tables', 'table', required=True)
    capacity = fields.Integer("Capacity")
    order_number = fields.Integer("Order #")
    order_date = fields.Date(string='Order Date', required=True)
    # current_date = fields.Datetime(string='Current Date and Time')
    order_customer = fields.Many2one('bp.food.customers', string ='Name of Customer')
    order_dish = fields.Many2one('food.dishtype', string='Dish to be Ordered')
    order_server = fields.Many2one('food.employees', string='Server/Waiter Name')
    order_amount = fields.Integer(string='Bill Total')
    order_comments = fields.Char('Add comments here for customisation or Allergies')


# Add Sale order line and computer fields for Bill here.

# @api.constrains('order_date')
#
#
# def _check_order_date(self):
#     if self.order_date <= self.current_date:
#         raise ValidationError('End date must be after Start Date')

#
# table = fields.One2many('food.tables', 'table',
#                                string='Table No. for Order')
#     capacity = fields.fields.One2many('food.tables', 'capacity',
#                                string='table capacity')
#     order_number = fields.Integer("Order #", required=True, index=True)
#     order_date = fields.Date(string='Order Date', required=True)
#     # current_date = fields.Datetime(string='Current Date and Time')
#     order_customer = fields.One2many('bp.food.customers', 'name',
#                                string='Name of Customer')
#     # order_dish = fields.Many2many('food.dish', 'dishes', string='Dish to be Ordered')
#     order_server = fields.One2many('food.employees', 'name',
#                                string='Name of Waiter/Server')
#     order_amount = fields.Integer(string='Bill Total')
#     order_comments = fields.Char('Add comments here for customisation or Allergies')
