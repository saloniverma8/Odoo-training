from odoo import fields, models, api
from datetime import datetime, timedelta


class Calendar(models.Model):
    _name = 'food.calendar'
    _description = 'calendar view of the restaurant tables'

    start_time = fields.Datetime(string='calendar Start Time', required=True
                                 , default=datetime.now())
    end_time = fields.Datetime(string='calendar End Time', required=True
                               , default=datetime.now())
    duration = fields.Char(compute='_calendar_duration',
                           string='Duration of calendar', required=True)
    server = fields.Many2one('food.employees', string='Server/Waiter Name')
    table = fields.Many2one('food.tables', 'Table No.')
    customer = fields.Many2one('res.partner', string='Name of Customer')


    @api.depends('start_time', 'end_time')
    def _calendar_duration(self):
        for per in self:
            calendar = per.end_time - per.start_time
            per.duration = timedelta(seconds=calendar.seconds)
