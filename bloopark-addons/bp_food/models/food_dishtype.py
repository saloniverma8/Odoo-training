import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api

class DishType(models.Model):
    _name = "food.dishtype"
    _description = "describes the different types of dishes that can be added"

    newdish = fields.Char(string="New Dish Name", required=True)
    dish_ingredients = fields.Char(string="Specify the Dish Ingredients")
    dish_type = fields.Selection(string='Dishes Type Veg/Non-Veg', selection=[
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
    ])
    dish_comments = fields.Char("Add Comments about Dish")



