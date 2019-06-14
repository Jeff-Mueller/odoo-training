# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Person(models.Model):
    _name = 'open_academy.person'
    _description = 'Person'
    
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    name = fields.Char(string='Name', compute='_get_name', store=True)   #Convention is to use _ at beginning of method for compute functions.
    
    #@api.multi
    #def name_get(self):
    #    return [
    #        (rec.id, "{} {}".format(rec.first_name, rec.last_name))
    #        for rec in self
    #    ]
    @api.depends('first_name', 'last_name')
    def _get_name(self):
        # data = self.name_get()
        for rec in self:
            # rec.name = data[rec.id]
            rec.name = "{} {}".format(rec.first_name, rec.last_name)
        