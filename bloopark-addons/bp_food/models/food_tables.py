# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FoodTables(models.Model):
    _name = 'food.tables'
    _description = 'Tables and Capacity in Restaurant'

    table = fields.Integer(string='Table Number', required=True, index=True)
    capacity = fields.Integer("Capacity")
    status = fields.Selection(string='Table Status', selection=[
        ('empty', 'Empty'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
        ('dirty', 'Dirty'),
    ])
    color = fields.Integer('Color Index', compute="change_colore_on_kanban")

    def change_colore_on_kanban(self):
         for record in self:
            color = 0
            if record.status == 'occupied':
                color = 2
            elif record.status == 'empty':
                color = 5
            elif record.cleaning_status == 'dirty':
                color = 7
            elif record.cleaning_status == 'reserved':
                color = 5
            else:
                color = 5
            record.color = color


