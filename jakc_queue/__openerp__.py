# -*- coding: utf-8 -*-
{
    'name': "Queue Management",

    'summary': """Queue Management System""",

    'description': """     
    """,

    'author': "Wahyu Hidayat",
    'website': "http://i-openerp.blogspot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'General',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/jakc_queue_view.xml',
        'views/jakc_queue_menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}