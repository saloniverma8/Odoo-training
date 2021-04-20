import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api


class RestEmployees(models.Model):
    _name = "food.employees"
    _description = "Employee Details"

    name = fields.Char("Name", required=True)
    emp_address = fields.Char("Address")
    emp_phone = fields.Integer("Employee Phone")
    # occupation_type = Many2one('food.employeestype', string='Occupation Type')
    occupation_type = fields.Selection([
        ('W', 'W - Waiter'),
        ('A', 'A - Accountant'),
        ('M', 'M - Manager'),
        ('N', 'N - Maintenance'),
        ('C', 'C - Chef')], string='Occupation of the Person in the Restaurant?')

