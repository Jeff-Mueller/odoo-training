# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Westros Training Academy""",

    'description': """
        Students will have a selection of classes where each class can have any number
        of teachers. The class will have a beginning and ending date so on and so
        forth. Students can sign up for the class and well have a grade at the end.
    """,

    'author': "Precision Solutions",
    'website': "http://www.precisonline.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Demo',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/open_academy_security.xml',
        'security/ir.model.access.csv',
        'views/open_academy_views.xml',
        'views/sale_order_inherit_form.xml',
        'views/menuitems.xml',
        'reports/sale_order_report_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': [
        'static/src/scss/bar_css.scss',
    ],
}