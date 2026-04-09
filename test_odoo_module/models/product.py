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

    def calculate_tax(self, tax_rate=0.1):
        """Calculate tax on price."""
        if tax_rate == 0:
            return 0.0
        tax = self.price * tax_rate
        return tax
