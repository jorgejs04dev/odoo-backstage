from odoo import models, fields


class Equipo(models.Model):
    _name = 'backstage.equipo'
    _description = 'Equipo audiovisual'

    name = fields.Char(string='Nombre', required=True)
    categoria = fields.Selection([
        ('camara', 'Cámara'),
        ('luz', 'Iluminación'),
        ('sonido', 'Sonido'),
        ('dron', 'Dron'),
    ], string='Categoría', required=True)
    precio_dia = fields.Float(string='Precio por día')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('alquilado', 'Alquilado'),
        ('reparacion', 'En el taller'),
    ], string='Estado', default='disponible')

    fecha_compra=fields.Date(string='Fecha de compra')

    notas=fields.Text(string='notas')

    active = fields.Boolean(string='Activo', default=True)
    
    imagen = fields.Image(string='Foto', max_width=1024,max_height=1024 )