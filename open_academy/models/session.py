# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'
    
    name = fields.Char(string='Session Name', required=True)
    course_id = fields.Many2one('open_academy.course', string='Course', required=True)
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    instructor = fields.Many2one('res.partner', string='Instructor')
    
    # students = fields.One2many('open_academy.person', 'session_id')
    
    course_name = fields.Char(compute='_compute_get_course_names')
    
    def _compute_course_names(self):
      courses = self.mapped("course_id")