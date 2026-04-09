# Pylint-Odoo: Odoo 18 Linting

### What it does:

Catches Odoo-specific Python issues: deprecated APIs, SQL injection, print statements, translation misuse, and manifest problems.

---

### 1. Use logger, not print (`print-used`)

#### ❌ Before

```python
class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        print("Order confirmed!")

        return super().action_confirm()
```

#### ✅ After

```python
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        _logger.info("Order confirmed!")
        return super().action_confirm()
```

---

### 2. SQL injection risk (`sql-injection`)

#### ❌ Before

```python
def get_partner(self, name):
    self.env.cr.execute(
        "SELECT id FROM res_partner WHERE name = '%s'" % name
    )
```

#### ✅ After

```python
def get_partner(self, name):
    self.env.cr.execute(
        "SELECT id FROM res_partner WHERE name = %s", (name,)
    )
```

---

### 3. Deprecated Warning class (`odoo-exception-warning`)

#### ❌ Before

```python
from odoo.exceptions import Warning

raise Warning("Amount must be positive!")
```

#### ✅ After

```python
from odoo.exceptions import UserError

raise UserError("Amount must be positive!")
```

---

### 4. Use `self.env._` in Odoo 18+ (`prefer-env-translation`)

#### ❌ Before

```python
from odoo import _

msg = _("Order %s confirmed", self.name)
```

#### ✅ After

```python
msg = self.env._("Order %s confirmed", self.name)
```

---

### 5. No `_()` in field definitions (`translation-field`)

#### ❌ Before

```python
from odoo import fields, _

custom_ref = fields.Char(string=_("Custom Ref"))
```

#### ✅ After

```python
from odoo import fields

custom_ref = fields.Char(string="Custom Ref")
```

---

### 6. Manifest: missing author (`manifest-required-author`)

#### ❌ Before

```python
{
    "name": "My Module",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
}
```

#### ✅ After

```python
{
    "name": "My Module",
    "version": "18.0.1.0.0",
    "author": "Odoo Community Association (OCA), My Company",
    "license": "LGPL-3",
    "depends": ["base"],
}
```

---

### 7. Manifest: remove default values (`manifest-superfluous-key`)

#### ❌ Before

```python
{
    "name": "My Module",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [],
    "installable": True,
}
```

#### ✅ After

```python
{
    "name": "My Module",
    "version": "18.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["base"],
}
```

---

### 8. Missing README (`missing-readme`)

#### ❌ Before

```
my_module/
├── __init__.py
├── __manifest__.py
```

#### ✅ After

```
my_module/
├── __init__.py
├── __manifest__.py
├── README.rst
```

---

**How to fix:** Read the error code in the output, find the matching example above, and apply the fix.
