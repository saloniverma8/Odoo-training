import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api

class EmployeesType(models.Model):
    _name = "food.employeestype"
    _description = "describes the different types of jobs a person can have at the restaurant"

    # occupation = fields.One2many('food.employees', string="Occupation Type Ex. Chef, Waiter", required=True)
    occupation = fields.Char(string='new job')

    comments = fields.Char(string="Add Comments about the job role")
