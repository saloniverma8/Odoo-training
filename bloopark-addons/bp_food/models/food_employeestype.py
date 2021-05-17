import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api

class EmployeesType(models.Model):
    _name = "food.employeestype"
    _description = "new_employee"

    # occupation = fields.One2many('food.employees', string="Occupation Type Ex. Chef, Waiter", required=True)
    name = fields.Char(string='New Job')
    occupation_type = fields.Selection([
        ('W', 'W - Waiter'),
        ('A', 'A - Accountant'),
        ('M', 'M - Manager'),
        ('N', 'N - Maintenance'),
        ('C', 'C - Chef')], string='Occupation of the Person in the Restaurant?')

    comments = fields.Char(string="Add Comments about the job role")
