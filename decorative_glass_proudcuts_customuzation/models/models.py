# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MatrialType(models.Model):
    _name = 'matrial.type'
    _description = 'Matrial Type'
    name = fields.Char('Name')

class MatrialGroup(models.Model):
    _name = 'matrial.group'
    _description = 'Matrial Group'
    name = fields.Char('Name')