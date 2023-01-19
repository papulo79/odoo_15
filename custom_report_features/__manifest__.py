# -*- coding: utf-8 -*-

{
    'name': "custom_report_features",
    'author': 'pdeandresconde.com',
    'category': 'Sale',
    'summary': 'Custom report features',
    'license': 'AGPL-3',
    'website': 'http://www.pdeandresconde.com',
    'description': """Custom report features""",
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
            'security/ir.model.access.csv',
            'view/view_company_form.xml',
            'report/sale_report.xml',
            'report/clean_layout_templates.xml',
            'report/sale_report_saleorder.xml',
    ],
    'images': ['static/description/company-logo.jpg'],
    'installable': True,
    'application': True,
    'assets': {}
}
