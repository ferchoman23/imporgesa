# -*- coding: utf-8 -*-
{
    'name': "Imporgesa",

    'summary': """ Imporgesa """,

    'description': """
        Imporgesa
    """,

    'author': "STECHNOLOGIES",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['product','base','sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_views.xml',
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        'views/account_report.xml',
        'report/reporte_cheque_bi_view.xml',
        'wizard/recuperacion_pagos_wizard_views.xml'
    ],
    'qweb': [
    ],
    'license': 'LGPL-3',
}
