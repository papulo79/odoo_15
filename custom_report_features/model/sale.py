# -*- coding: utf-8 -*-

from odoo import api, fields, models
import json


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Example of custom computed field for the report
    tax_totals_json2 = fields.Char(
        compute='_compute_tax_totals_json2', default='{}')

    # If you need to do some custom operations in one report, define the variable and calculate it.
    # It only be calculated when the user print it, maybe for calculate stock in real time or similar.
    def _compute_tax_totals_json2(self):
        for order in self:
            order.tax_totals_json2 = '{}'

    # Sometimes, the reports had a function that retrieves some info and you need to manipulate the result before print it
    # In order to extend it, define the method an call the parent with "super"
    def order_lines_layouted(self):
        report_pages = super(SaleOrder, self).order_lines_layouted()
        # Now you can manipulate the result before send it to the template
        return report_pages


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    report_description = fields.Text(
        'report_description', compute='_compute_report_description')

    def _compute_report_description(self):
        for record in self:
            record.report_description = record.name.replace(
                record.product_id.display_name+'\n', '')
