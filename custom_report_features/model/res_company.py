# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, exceptions
import logging
_logger = logging.getLogger(__name__)


class ProjectTaskTemplateMarketingTimesheet(models.Model):
    _inherit = 'res.company'

    report_footer_bunit2 = fields.Text(string="Business Unit")


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    report_footer_bunit2 = fields.Text(
        related='company_id.report_footer_bunit2', readonly=False, default='', string="Business Unit", compute='_compute_report_footer_bunit2')

    @api.onchange('report_footer_bunit2')
    def _onchange_report_footer_bunit2(self):
        for wizard in self:
            company = wizard.company_id
            if wizard.report_footer_bunit2 and wizard.report_footer_bunit2 != '':
                company.report_footer_bunit2 = wizard.report_footer_bunit2
            wizard.report_footer_bunit2 = company.report_footer_bunit2

    @api.depends('company_id.report_footer_bunit2')
    def _compute_report_footer_bunit2(self):
        for wizard in self:
            company = wizard.company_id
            wizard.report_footer_bunit2 = company.report_footer_bunit2
