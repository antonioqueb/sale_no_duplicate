from odoo import models, exceptions

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def copy(self, default=None):
        """
        Sobrescribe el método copy para restringir
        la duplicación de registros de venta.
        """
        raise exceptions.UserError(
            'La duplicación de pedidos de venta está restringida.'
        )
        # En caso de que quieras permitir duplicar con
        # ciertas condiciones, añade la lógica condicional
        # aquí. De lo contrario, simplemente se lanza el error.
        # return super(SaleOrder, self).copy(default)
