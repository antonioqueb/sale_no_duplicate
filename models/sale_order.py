from odoo import models, exceptions

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def copy(self, default=None):
        """
        Sobrescribe el método `copy` para permitir la duplicación
        solo a usuarios pertenecientes al grupo "Allow Sale Duplicates".
        """
        # Verifica si el usuario actual está en el grupo que habilita la duplicación
        if not self.env.user.has_group('sale_no_duplicate.group_sale_duplicate_allowed'):
            raise exceptions.UserError(
                'No tienes permiso para duplicar este pedido de venta.'
            )
        return super(SaleOrder, self).copy(default)
