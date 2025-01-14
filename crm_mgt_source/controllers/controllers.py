# -*- coding: utf-8 -*-
# from odoo import http


# class CrmMgtSource(http.Controller):
#     @http.route('/crm_mgt_source/crm_mgt_source', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_mgt_source/crm_mgt_source/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_mgt_source.listing', {
#             'root': '/crm_mgt_source/crm_mgt_source',
#             'objects': http.request.env['crm_mgt_source.crm_mgt_source'].search([]),
#         })

#     @http.route('/crm_mgt_source/crm_mgt_source/objects/<model("crm_mgt_source.crm_mgt_source"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_mgt_source.object', {
#             'object': obj
#         })
