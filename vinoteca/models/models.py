from odoo import models, fields, api

class Bodega(models.Model):
    _name = 'vinoteca.bodega'

    name = fields.Char(string="Bodega", required=True)
    description = fields.Text(string="Información adicional")

    productos_ids = fields.One2many('vinoteca.producto', 'bodega_id', string="Productos")


class Producto(models.Model):
    _name = 'vinoteca.producto'

    name = fields.Char(string="Nombre del producto", required=True)
    code = fields.Char(string="Codigo", required=True)
    price = fields.Float(string="Precio", digits=(4, 2), required=True)
    typeContainer = fields.Char(string="Tipo de envase", required=True)

    bodega_id = fields.Many2one('vinoteca.bodega', ondelete='cascade', string="Bodega")

    compras_ids = fields.Many2many('vinoteca.compra', string="Compras")


class Zumo(models.Model):
    _name = 'vinoteca.zumo'
    _inherit = 'vinoteca.producto'

    sugar = fields.Float(string="Cantidad de azucar", digits=(2, 2), help="En gr por cada 100ml", required=True)
    pulpa = fields.Boolean(string="Pulpa", required=True)


class Cliente(models.Model):
    _name = 'vinoteca.cliente'

    name = fields.Char(string="Nombre", required=True)

    compras_ids = fields.One2many('vinoteca.compra', 'cliente_id', string="Compras")


class Compra(models.Model):
    _name = 'vinoteca.compra'

    code = fields.Char(string="Codigo", required=True)
    date = fields.Date(string="Fecha de compra", required=True)

    cliente_id = fields.Many2one('vinoteca.cliente', ondelete='cascade', string="Cliente")

    productos_ids = fields.Many2many('vinoteca.producto', string="Productos")