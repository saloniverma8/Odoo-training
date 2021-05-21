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



