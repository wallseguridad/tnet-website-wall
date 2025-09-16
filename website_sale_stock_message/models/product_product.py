from odoo import models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_stock_message(self):
        return self.product_tmpl_id.get_stock_message()