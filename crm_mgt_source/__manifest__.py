# -*- coding: utf-8 -*-
{
    'name': 'CRM Marketing Source',
    'version': '16.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Sales',
    'summary': 'Adds "MKT Source" submenu to CRM Settings for managing utm.sources.',
    'depends': ['crm'],
    'data': [
        'views/utm_source_views.xml',    # Listagem de utm.source com edição in-line
        'views/segment_type_menu.xml',   # Menu de Configuração "MKT Source"
        'security/ir.model.access.csv',  # Regras de segurança para o modelo utm.source
    ],
    'installable': True,
    'application': False,
}
