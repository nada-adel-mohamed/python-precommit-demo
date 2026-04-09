import logging
from odoo import fields, models


_logger = logging.getLogger(__name__)


class TestCategory(models.Model):
    """A simple category model."""

    _name = "test.category"
    _description = "Test Category"
    _order = "name asc"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Description")
    code = fields.Char(string="Category Code", unique=True)
    active = fields.Boolean(default=True)

    def action_archive(self):
        """Archive the category."""
        self.write({"active": False})
        _logger.info("Category %s archived", self.name)
        return True

    def action_unarchive(self):
        """Unarchive the category."""
        self.write({"active": True})
        _logger.info("Category %s unarchived", self.name)
        return True
