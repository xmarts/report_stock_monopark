# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reporte(models.Model):
	_name = 'reporte.clientes'
	
	nombre = fields.Char(string="Nombre")
	paterno = fields.Char(string="Apellido paterno")
	materno = fields.Char(string="Apellido materno")