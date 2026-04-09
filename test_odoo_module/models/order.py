import logging
from odoo import fields, models


_logger = logging.getLogger(__name__)


class TestOrder(models.Model):
    """A model to represent test orders."""

    _name = "test.order"
    _description = "Test Order"
    _order = "date_order desc"

    name = fields.Char(string="Order Reference", required=True, copy=False)
    date_order = fields.Datetime(string="Order Date", default=fields.Datetime.now, required=True)
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    amount_total = fields.Float(string="Total Amount", compute="_compute_amount_total", store=True)
    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed"), ("done", "Done")],
        string="Status",
        default="draft",
    )
    active = fields.Boolean(default=True)

    def _compute_amount_total(self):
        """Compute the total amount."""
        for record in self:
            record.amount_total = 0.0  # Placeholder computation

    def action_confirm(self):
        """Confirm the order."""
        self.write({"state": "confirmed"})
        _logger.info("Order %s confirmed", self.name)
        return True
