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
    code = fields.Char(string="Category Code")
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("code_unique", "unique(code)", "Category code must be unique."),
    ]

    def action_archive(self):
        """Archive the category."""
        self.write({"active": False})
        _logger.info("Categories archived: %s", ", ".join(self.mapped("name")))
        return True

    def action_unarchive(self):
        """Unarchive the category."""
        self.write({"active": True})
        _logger.info("Categories unarchived: %s", ", ".join(self.mapped("name")))
        return True
