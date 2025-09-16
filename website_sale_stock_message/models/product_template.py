from odoo import fields, models, _
from markupsafe import Markup


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    show_stock_message_1 = fields.Boolean(string='Show Stock High', default=False)
    stock_message_1_condition = fields.Float(string="Message Condition")
    stock_message_1 = fields.Text(string="Message")

    show_stock_message_2 = fields.Boolean(string='Show Medium Stock', default=False)
    stock_message_2_condition_1 = fields.Float(string="Message Condition(1)")
    stock_message_2_condition_2 = fields.Float(string="Message Condition(2)")
    stock_message_2 = fields.Text(string="Message")

    show_stock_message_3 = fields.Boolean(string='Show Low Stock', default=False)
    stock_message_3_condition_1 = fields.Float(string="Message Condition(1)")
    stock_message_3_condition_2 = fields.Float(string="Message Condition(2)")
    stock_message_3 = fields.Text(string="Message")

    show_stock_message_4 = fields.Boolean(string='Show Out of Stock', default=False)
    stock_message_4_condition = fields.Float(string="Message Condition")
    stock_message_4 = fields.Text(string="Message")

    def get_stock_message(self):
        self = self.sudo()
        website = self.env['website'].get_current_website()
        rec = self if self._name == 'product.product' else self.product_variant_id
        qty = rec.with_context(warehouse=website.warehouse_id.id).sudo().qty_available
        t = self if self._name == 'product.template' else self.product_tmpl_id
        parts = []
        if t.show_stock_message_1 and qty >= t.stock_message_1_condition:
            parts.append(f'<span class="badge badge-success">{t.stock_message_1}</span>')
        elif t.show_stock_message_2 and qty >= t.stock_message_2_condition_2 and qty <= t.stock_message_2_condition_1:
            parts.append(f'<span class="badge badge-warning">{t.stock_message_2}</span>')
        elif t.show_stock_message_3 and qty >= t.stock_message_3_condition_2 and qty <= t.stock_message_3_condition_1:
            parts.append(f'<span class="badge badge-danger">{t.stock_message_3}</span>')
        elif t.show_stock_message_4 and qty <= t.stock_message_4_condition:
            parts.append(f'<span class="badge badge-danger">{t.stock_message_4}</span>')
        return Markup('<div class="website_sale_stock-badge">' + ''.join(parts) + '</div>')
