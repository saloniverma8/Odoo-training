from odoo import fields, models, api
from odoo.exceptions import ValidationError


class CheckBookingWizard(models.TransientModel):
    _name = 'check.booking.table'

    name = fields.Char("name")
    customer = fields.Many2one('res.partner')
    request_start_date = fields.Datetime("Request Start DateTime")
    request_end_date = fields.Datetime("Request End DateTime")
    available_table = fields.Many2one('food.tables')
    request_table = fields.Char('table no')
    request_status = fields.One2many(related='request_table.status',
                                     string='Table Status', readonly=True)

    def check_table(self):
        print('6666666666666666666666666666')
        return True


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
