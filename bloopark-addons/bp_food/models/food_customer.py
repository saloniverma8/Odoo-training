# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FoodCustomers(models.Model):
    _name = 'bp.food.customers'
    _description = 'table for customer data'

    name = fields.Char("Customer Name", required=True)
    number = fields.Char("Phone Number")
    email = fields.Char("Email")

# @api.depends('value')


# def _value_pc(self):
#     for record in self:
#         record.value2 = float(record.value) / 100
#
#         #function for saving values in DB
