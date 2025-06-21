# -*- coding: utf-8 -*-
# from odoo import http


# class UomNoConversion(http.Controller):
#     @http.route('/uom_no_conversion/uom_no_conversion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uom_no_conversion/uom_no_conversion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('uom_no_conversion.listing', {
#             'root': '/uom_no_conversion/uom_no_conversion',
#             'objects': http.request.env['uom_no_conversion.uom_no_conversion'].search([]),
#         })

#     @http.route('/uom_no_conversion/uom_no_conversion/objects/<model("uom_no_conversion.uom_no_conversion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uom_no_conversion.object', {
#             'object': obj
#         })

