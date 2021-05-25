from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class FoodTables(models.Model):
    _name = 'food.tables'
    _description = 'Tables and Capacity in Restaurant'

    name = fields.Char(string='Table', copy=False,
                       readonly=True, index=True,
                       default=lambda self: 'New')
    capacity = fields.Integer("Capacity")
    status = fields.Selection(
        [
            ('empty', 'Empty'),
            ('occupied', 'Occupied'),
            ('reserved', 'Reserved'),
            ('dirty', 'Dirty'),
        ],
        index=True,
        default="occupied")

    start_time = fields.Datetime(string='calendar Start Time', default=datetime.now())
    end_time = fields.Datetime(string='calendar End Time', default=datetime.now())
    duration = fields.Char(compute='_calendar_duration',
                           string='Duration of calendar')
    server = fields.Many2one('hr.employee', string='Server/Waiter Name')
    customer = fields.Many2one('res.partner', string='Name of Customer')

    _sql_constraint_0 = [('id_uniq', 'unique(name)',
                          'The table is already booked!')]

    @api.depends('start_time', 'end_time')
    def _calendar_duration(self):
        for per in self:
            calendar = per.end_time - per.start_time
            per.duration = timedelta(seconds=calendar.seconds)

    # color = fields.Integer('Color Index', compute="change_colore_on_kanban")
    member_color = fields.Integer(compute='_check_color')
    color = fields.Integer(string='color')

    def check(self):
        print('6666666666666666666666666666')
        return True

    def _check_color(self, status):
        for name in self:
            color = 0
            if name.status == 'occupied':
                color = 2
            elif name.status == 'empty':
                color = 5
            elif name.status == 'reserved':
                color = 7
            else:
                color = 5
            name.color = color

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'food.tables.sequence') or 'New'
        result = super(FoodTables, self).create(vals)
        return result

    # @api.model
    # def action_set_to_draft(self):
    #     """
    #     This method is used to change the state
    #     to draft of the hotel restaurant reservation
    #     --------------------------------------------
    #     @param self: object pointer
    #     """
    #
    #     self.status = "empty"
    #     return True

    # def table_reserved(self):
    #     """This method is used to book only one table at a time"""
    #     if self.status ='occupied'
    #         self.name =

    @api.constrains('start_time', 'end_time')
    def _check_table_time(self):
        print('------------------------------------------------------')
        if self.end_time <= self.start_time:
            print(self.start_time)
            print(self.end_time)
            raise ValidationError('End time must be after Start time')

    @api.constrains('start_time')
    def _check_table_date(self):
        print('------------------------------------------------------')
        if self.start_time <= datetime.now():
            raise ValidationError('Start time cannot be before Current Time')

    @api.constrains('name', 'end_time')
    def _check_table_allow(self):
        if self.start_time <= datetime.now():
            raise ValidationError('Start time cannot be before Current Time')



# add check for capacity
#     add check for allowing to sit only on tables that are empty
# when the time is over, set status of table back to empty and available and green
# do not set capacity more than 10 for a table
# do not allow previous date reservations
# do not allow reservations before today's date and time
