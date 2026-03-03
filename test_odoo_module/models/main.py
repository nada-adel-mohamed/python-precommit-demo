from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)


class TestModel(models.Model):
    """A model used to demonstrate and verify pre-commit hook fixes."""

    _name = "test.model"
    _description = "Test Model"

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)

    def action_test(self):
        """Perform a test action while following Odoo 18 best practices."""
        # FIX: Replaced print with logger
        _logger.info("Testing hook...")

        # FIX: Prevented SQL injection by using parameters
        self.env.cr.execute("SELECT id FROM res_partner WHERE name = %s", (self.name,))

        # FIX: Used self.env._ and lazy formatting for Odoo 18+
        msg = self.env._("Testing translation for %s", self.name)

        _logger.info(msg)

        return True
