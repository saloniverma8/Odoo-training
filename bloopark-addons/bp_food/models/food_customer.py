# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'customer'

    test = fields.Char()

    orientation = fields.Selection([
        ('v', 'Vegan'),
        ('g', 'Vegetarian'),
        ('p', 'Pescatarian'),
        ('n', 'Non-Vegetarian'),
    ], string='Veg/Non-Veg')

    # frequency = fields.Selection([
    #     ('f', 'Frequent'),
    #     ('i', 'Intermediate'),
    #     ('r', 'Rare'),
    #     ('t', 'First Time'),
    #     ], string='Frequency')
