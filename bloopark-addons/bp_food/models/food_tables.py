# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


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

    start_time = fields.Datetime(string='calendar Start Time', required=True
                                 , default=datetime.now())
    end_time = fields.Datetime(string='calendar End Time', required=True
                               , default=datetime.now())
    duration = fields.Char(compute='_calendar_duration',
                           string='Duration of calendar', required=True)
    server = fields.Many2one('food.employees', string='Server/Waiter Name')
    customer = fields.Many2one('bp.food.customers', string='Name of Customer')

    @api.depends('start_time', 'end_time')
    def _calendar_duration(self):
        for per in self:
            calendar = per.end_time - per.start_time
            per.duration = timedelta(seconds=calendar.seconds)

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


