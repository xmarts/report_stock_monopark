# -*- coding: utf-8 -*-
{
    'name': "report_mod_mono",

    'summary': """
        Generate reports by filters.
    """,

    'description': """
        Generate reports by filters whether product, category, warehouse or general.
    """,

    'author': "Xmarts",
    'Collaborators:' "Gilbert santiago acevedo, Marco Aguilar"
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock, Products',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/layout.xml',
        'reports/report_stock.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}