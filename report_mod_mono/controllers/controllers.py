# -*- coding: utf-8 -*-
from odoo import http

# class ReportModMono(http.Controller):
#     @http.route('/report_mod_mono/report_mod_mono/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_mod_mono/report_mod_mono/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_mod_mono.listing', {
#             'root': '/report_mod_mono/report_mod_mono',
#             'objects': http.request.env['report_mod_mono.report_mod_mono'].search([]),
#         })

#     @http.route('/report_mod_mono/report_mod_mono/objects/<model("report_mod_mono.report_mod_mono"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_mod_mono.object', {
#             'object': obj
#         })