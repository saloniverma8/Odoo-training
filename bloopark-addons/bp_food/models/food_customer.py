# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FoodCustomers(models.Model):
    _name = 'bp.food.customers'
    _description = 'table for customer data'

    name = fields.Many2one('food.order', string="Customer Name", required=True,
                                ondelete='cascade')
    number = fields.Integer("Phone Number")
    email = fields.Char("Email")

    # @api.depends('number')
    #
    #
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    #
    #         #function for saving values in DB


@api.constrains('number')
def check_number(self):
    for rec in self:
        if len(rec.number)<12:
            raise ValidationError('Mobile Number incorrect. More number of expected fields')
