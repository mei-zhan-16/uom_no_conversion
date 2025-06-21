# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class uom_no_conversion(models.Model):
#     _name = 'uom_no_conversion.uom_no_conversion'
#     _description = 'uom_no_conversion.uom_no_conversion'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

