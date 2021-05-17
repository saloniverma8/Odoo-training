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
    table = fields.Many2one('food.tables', 'Table No.', required=True)
    capacity = fields.Integer("Capacity")
    order_number = fields.Integer("Order #")
    order_date = fields.Date(string='Order Date', required=True)
    # current_date = fields.Datetime(string='Current Date and Time')
    order_customer = fields.Many2one('bp.food.customers', string='Name of Customer')
    order_dish = fields.Many2one('food.dishtype', string='Dish to be Ordered')
    # sale_order_ids = fields.One2many('sale.order', 'sale_id',
    #                                  string='Food Sales')
    # sales_count = fields.Integer(compute='_compute_sales_course')
    order_server = fields.Many2one('food.employees', string='Server/Waiter Name')
    order_amount = fields.Integer(string='Bill Total')
    order_comments = fields.Char('Add comments here for customisation or Allergies')


@api.constrains('order_date')
def _check_order_date(self):
    if self.order_date <= datetime.now():
        raise ValidationError('Start date must be after today.')
