import logging
from odoo import fields, models


_logger = logging.getLogger(__name__)


class TestCategory(models.Model):
    """A simple category model."""

    _name = "test.category"
    _description = "Test Category"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)
