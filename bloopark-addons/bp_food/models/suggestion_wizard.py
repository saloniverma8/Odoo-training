from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CheckBookingWizard(models.Model):
    _name = 'check.booking.table'
    _description = "Booking"

    current_tables = fields.Many2many('food.tables')
    current_table_end = fields.Datetime(related='current_tables.end_time',
                                           string='Booked End Table', readonly=True)
    name = fields.Char("name")
    customer = fields.Many2one('res.partner')
    request_start_date = fields.Datetime("Request Start DateTime")
    request_end_date = fields.Datetime("Request End DateTime")
    existing_table = fields.Many2one('food.tables')
    available_table = fields.Datetime(related='existing_table.end_time')
    # request_table = fields.Char('table no')
    # available_table = fields.Selection(selection='_check_table', string='Available Table')
    # request_status = fields.One2many(related='request_table.status',
    #                                  string='Table Status', readonly=True)
    request_status = fields.Char("status")

    def _check_table(self):
        tables = list()
        tables.append(("20", "20"))
        tables.append(("21", "21"))
        return tables


        # for rec in self:
        # for rec.request_table:
        #     raise ValidationError('table can be booked')
        # else:
        #     raise ValidationError('table cannot be booked')


        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'food.tables.booking',
        #     'view_mode': 'form',
        #     'res_model': 'food.tables',
        #     'res_id': available_table,
        #     'target': 'current',
        #     'context': {
        #         'form_view_initial_mode': 'edit',
        #                 },
        #         }
