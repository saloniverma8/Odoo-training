from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class FoodDishAvail(models.Model):
    _name = "food.dishavailable"
    _description = "Dishes Offered"

    dishesavail = fields.Selection(string='Dishes Offered', selection=[
        ('shahi', 'Shahi Paneer'),
        ('chicken', 'Butter Chicken'),
    ])

    # shahipaneeringredients = fields.Selection(string='Shahi Paneer Ingredients', selection=[
    #     ('Tomatoes', 'Tomatoes 100 gms'),
    #     ('Onions', 'Onions 70 gms'),
    #     ('spices', 'Indian Spices 2 gms'),
    #     ('cottagecheese', 'Cottage Cheese 60 gms'),
    #     ('creamsahne', 'Cream/Sahne 15 gms'),
    # ], default='1')
    #
    # chickeningredients = fields.Selection(string='Butter Chicken Ingredients', selection=[
    #     ('Chicken', 'Chicken Breast 200 gms'),
    #     ('ispices', ' Indian Spices 5 gms'),
    #     ('preservedmarinate', ' Preserved Marinate 100 gms'),
    #     ('garnishing', 'Garnishing 10 gms'),
    #     ('butter', 'Butter 30 gms'),
    ])
    # curry_ingredients = fields.Selection(string='Butter Chicken Ingredients', selection=[
    #     ('Curd/Yogurt', '100 gms'),
    #     ('Salt', '100 gms'),
    #     ('Gram Flour', '100 gms'),
    #     ('Indian Spices', '100 gms'),
    #     ('Dried Leaves', '100 gms'),
    # ])
    # naan_ingredients = fields.Selection(string='Butter Chicken Ingredients', selection=[
    #     ('Flour', '100 gms'),
    #     ('Salt', '100 gms'),
    #     ('Baking powder', '100 gms'),
    #     ('Oil', '100 gms'),
    #     ('Orders', '100 gms'),
    # ])
    # mangolassi_ingredients = fields.Selection(string='Butter Chicken Ingredients', selection=[
    #     ('Flour', '100 gms'),
    #     ('Salt', '100 gms'),
    #     ('Baking powder', '100 gms'),
    #     ('Oil', '100 gms'),
    #     ('Orders', '100 gms'),
    # ])

