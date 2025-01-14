# -*- coding: utf-8 -*-
{
    'name': 'CRM Marketing Source',
    'version': '16.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': 'Adds "MKT Source" submenu to CRM Settings for managing utm.sources.',
    'author': 'Ananias Filho',
    'depends': ['crm'],
    'data': [
        'views/utm_source_views.xml',
        'views/segment_type_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
