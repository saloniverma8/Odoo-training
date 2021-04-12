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

    table = fields.Char("Table Number", required=True, index=True)
    capacity = fields.Integer("Capacity")
    order_number = fields.Integer("Order #")
    order_date = fields.Date(string='Order Date', required=True)
    # order_customer = fields.One2many('bp.food.customers', 'name', string ='Name of Customer')
    # order_dish = fields.Many2many('food.dish', 'dishes', string='Dish to be Ordered')
    # order_server = fields.Many2one('food.employees', 'name', string='Server/Waiter Name')
    order_amount = fields.Integer(string='Bill Total $30')
    order_comments = fields.Char('Add comments here for customisation or Allergies')

 # Add Sale order line and computer fields for Bill here.

