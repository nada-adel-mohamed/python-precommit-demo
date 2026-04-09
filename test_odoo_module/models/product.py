import logging
from odoo import fields, models


_logger = logging.getLogger(__name__)


class TestProduct(models.Model):
    """A simple product model."""

    _name = "test.product"
    _description = "Test Product"

    name = fields.Char(string="Product Name", required=True)
    price = fields.Float(string="Price", required=True)
    active = fields.Boolean(default=True)

    def calculate_tax(self):
        """Calculate tax on price."""
        # BUG: Division by zero when tax_rate is 0
        tax_rate = 0
        tax = self.price / tax_rate
        return tax
