from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class DemoSequence(models.Model):
    _name = 'demo.sequence'
    _description = 'Demo Sequence'

    name = fields.Char(string='Name', required=True)

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('demo.sequence') or '/'
        vals['name'] = '{}_{}'.format(seq, vals['name'])
        new_record = super().create(vals)
        return new_record


class DemoScheduler(models.Model):
    _name = 'demo.scheduler'
    _description = 'Demo Scheduler'

    def action_schedule(self):
        _logger.warning('============= Action Schedule ==================')
