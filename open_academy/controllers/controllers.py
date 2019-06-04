# -*- coding: utf-8 -*-
from odoo import http

# class Src/user/openAcademy(http.Controller):
#     @http.route('/src/user/open_academy/src/user/open_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/src/user/open_academy/src/user/open_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('src/user/open_academy.listing', {
#             'root': '/src/user/open_academy/src/user/open_academy',
#             'objects': http.request.env['src/user/open_academy.src/user/open_academy'].search([]),
#         })

#     @http.route('/src/user/open_academy/src/user/open_academy/objects/<model("src/user/open_academy.src/user/open_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('src/user/open_academy.object', {
#             'object': obj
#         })