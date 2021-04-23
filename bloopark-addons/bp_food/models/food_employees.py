import time

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

from odoo import models, fields, api


class RestEmployees(models.Model):
    _name = "food.employees"
    _description = "Employee Details"

    # name = fields.Many2one('food.order', string="Server Name", ondelete='cascade')
    name = fields.Char(string="Employee Name")
    emp_address = fields.Char("Address")
    emp_phone = fields.Integer("Employee Phone")
    occupation = fields.Many2one('food.employeestype', string='Occupation Type',
                                 ondelete='set null')

    occupation_type = fields.Selection([
        ('W', 'Waiter'),
        ('A', 'Accountant'),
        ('M', 'Manager'),
        ('N', 'Maintenance'),
        ('C', 'Chef')], string='Department to Which He Belongs')