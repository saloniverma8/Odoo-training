import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date

from odoo import models, fields, api


class FoodOrder(models.Model):
    _inherit = "lunch.order"
    _description = "Order"

    # table = fields.One2many('food.tables', 'table', required=True, index=True)
    # name = fields.Integer(required=True, index=True, string='Order No. ')
    table = fields.Many2one('food.tables', 'Table No.')
    capacity = fields.Integer("Capacity")
    order_number = fields.Integer("Order #")
    order_date = fields.Date(string='Order Date')
    # current_date = fields.Datetime(string='Current Date and Time')
    order_customer = fields.Many2one('res.partner', string='Name of Customer')
    order_dish = fields.Many2one('food.dishtype', string='Dish to be Ordered')
    # sale_order_ids = fields.One2many('sale.order', 'sale_id',
    #                                  string='Food Sales')
    # sales_count = fields.Integer(compute='_compute_sales_course')
    # order_server = fields.Many2one('hr.employee', string='Server/Waiter Name')
    # order_amount = fields.Integer(string='Bill Total')
    order_comments = fields.Char('Add comments here for customisation or Allergies')



#
# class BPOrder(models.Model):
#     _name = "food.order"
#     _description = "Orders"
#
#     # table = fields.One2many('food.tables', 'table', required=True, index=True)
#     name = fields.Integer(required=True, index=True, string='Order No. ')
#     table = fields.Many2one('food.tables', 'Table No.')
#     capacity = fields.Integer("Capacity")
#     order_number = fields.Integer("Order #")
#     order_date = fields.Date(string='Order Date')
#     # current_date = fields.Datetime(string='Current Date and Time')
#     order_customer = fields.Many2one('res.partner', string='Name of Customer')
#     order_dish = fields.Many2one('food.dishtype', string='Dish to be Ordered')
#     # sale_order_ids = fields.One2many('sale.order', 'sale_id',
#     #                                  string='Food Sales')
#     # sales_count = fields.Integer(compute='_compute_sales_course')
#     order_server = fields.Many2one('hr.employee', string='Server/Waiter Name')
#     order_amount = fields.Integer(string='Bill Total')
#     order_comments = fields.Char('Add comments here for customisation or Allergies')