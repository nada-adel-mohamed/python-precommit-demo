# Odoo 18 Gold Standard: Ruff & Prettier

### What it does:

This modern stack uses **Ruff** for ultra-fast Python formatting/linting and **Prettier** for specialized Odoo XML formatting. It is the current state-of-the-art for OCA Odoo 18 development.

---

### 1. Ruff: Auto-Formatting & Import Sorting (Replaces Black/Isort)

#### ❌ Before (Messy imports & formatting)

```python
from odoo import models,fields
import os
from odoo import api

class MyModel(models.Model):
    _name='my.model'
    def my_method(self):
        x = { 'a':1,'b':2 }
        return x
```

#### ✅ After (Clean, standardized code)

```python
import os

from odoo import api, fields, models


class MyModel(models.Model):
    _name = "my.model"

    def my_method(self):
        x = {"a": 1, "b": 2}
        return x
```

---

### 2. Prettier: XML Formatting (with plugin-xml)

#### ❌ Before (Inconsistent XML)

```xml
<record id="view_id" model="ir.ui.view">
<field name="name">view.name</field>
<field name="model">my.model</field>
<field name="arch" type="xml">
<form>
<sheet>
<group>
<field name="name"  />
<field name="active"/></group>
</sheet>
</form>
</field>
</record>
```

#### ✅ After (Perfectly indented & ordered)

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<record id="view_id" model="ir.ui.view">
    <field name="name">view.name</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name" />
                    <field name="active" />
                </group>
            </sheet>
        </form>
    </field>
</record>
```

---

### 3. Maintainer Tools: README Generation

#### ❌ Before (Hand-written README or missing)

_Manually maintaining `README.rst` with dynamic content like contributors and authors._

#### ✅ After (Auto-generated from fragments)

_The hook `oca-gen-addon-readme` automatically builds a professional `README.rst` using fragments from the `readme/` directory (Description, Credits, Usage, etc.)._

---

### 4. Ruff: Catching Logic Errors (Replaces Flake8)

#### ❌ Before

```python
def check_value(self):
    unused_var = 10  # Error: Assigned but never used
    if self.id == self.id:  # Error: Pointless comparison
        return True
```

#### ✅ After

```python
def check_value(self):
    return True
```

---

### 5. Pylint-Odoo: Mandatory vs Optional Checks

The config now runs **two passes**:

1. **Pass 1 (Optional)**: Runs all checks with `verbose: true` and `--exit-zero`. It shows you everything but won't block the commit.
2. **Pass 2 (Mandatory)**: Blocks the commit if any major Odoo-specific violations are found.

---

**How to fix:** Most of these are **auto-fixed** by Pre-commit!

- **Ruff** will fix your Python files automatically.
- **Prettier** will fix your XML/SCSS/JS files automatically.
  Just run `python -m pre_commit run --all-files` and then `git add` the changes!
