from odoo import api,models



class StockDeliveryNoteCreateWizard(models.TransientModel):
    _inherit = "stock.delivery.note.create.wizard"


    @api.onchange("partner_id")
    def _onchange_partner(self):
        partner_ids = (self.partner_id | self.partner_id.child_ids).sorted(lambda l:l.type=='delivery',reverse=True)
        self.partner_shipping_id = partner_ids[:1]