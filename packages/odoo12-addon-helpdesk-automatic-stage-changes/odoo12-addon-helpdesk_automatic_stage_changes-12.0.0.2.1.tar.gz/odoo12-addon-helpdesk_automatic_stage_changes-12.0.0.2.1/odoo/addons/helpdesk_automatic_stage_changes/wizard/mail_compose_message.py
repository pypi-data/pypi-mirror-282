# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api


class MailComposeMessage(models.TransientModel):
    _inherit = "mail.compose.message"

    when_odoo_responds_change_stage_to_id = fields.Many2one(
        "helpdesk.ticket.stage", string="Change stage to (When Odoo responds)"
    )

    @api.model
    def default_get(self, fields):
        result = super(MailComposeMessage, self).default_get(fields)
        if result.get("composition_mode") and result["composition_mode"] == "comment":
            result["subject"] = self._context.get("default_subject", result["subject"])
        return result

    @api.multi
    def action_send_mail(self):
        if (
            self.model == "helpdesk.ticket"
            and self.when_odoo_responds_change_stage_to_id
            and self.composition_mode == "mass_mail"
        ):
            ticket = self.env[self.model].browse(self.res_id)
            vals = {
                "when_odoo_responds_change_stage_to_id": self.when_odoo_responds_change_stage_to_id.id,  # noqa: E501
                "stage_id": self.when_odoo_responds_change_stage_to_id.id,
            }
            ticket.write(vals)
        return super(MailComposeMessage, self).action_send_mail()

    @api.multi
    @api.onchange('template_id')
    def onchange_template_id_wrapper(self):
        # Prevent onchange from messing with defaults when the template is set from
        # the mass mailing wizard in the helpdesk ticket form view
        if self._context and self._context.get('skip_onchange_template_id'):
            return
        super(MailComposeMessage, self).onchange_template_id_wrapper()
