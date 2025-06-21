from odoo import models, fields,api,_

class StockMove(models.Model):
    _inherit = 'stock.move'
   

    @api.model
    def create(self, vals):
        """Ensure the stock move uses the original UOM and quantity."""
        if vals.get('origin') and vals.get('sale_line_id'):
            print(f"{vals.get('origin')} this is Origin****{vals.get('sale_line_id')}this is saleline ID****************")
            print(f"{vals} this is value**********************************************")

            sale_line = self.env['sale.order.line'].browse(vals['sale_line_id'])
            if sale_line:
                vals.update({
                    'product_uom': sale_line.product_uom.id,  # Set original UOM
                    
                    'product_uom_qty': sale_line.product_uom_qty,  # Set original quantity
                    })
                
        return super(StockMove, self).create(vals)