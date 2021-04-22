# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FoodTables(models.Model):
    _name = 'food.tables'
    _description = 'Tables and Capacity in Restaurant'

    table = fields.Integer("Table Number", required=True, index=True)
    capacity = fields.Integer("Capacity")

    # @api.depends('number')
    #
    #
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    #
    #         #function for saving values in DB


# @api.constrains('number')
# def check_number(self):
#     for rec in self:
#         if len(rec.number)<12:
#             raise ValidationError('Mobile Number incorrect. More number of expected fields')