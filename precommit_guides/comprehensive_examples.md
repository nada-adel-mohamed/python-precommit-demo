# Odoo 18 Pre-commit: The Master Example Guide

This guide shows exactly how your code is transformed by the new pre-commit stack. Look for the ❌ **Before** and ✅ **After** for every major tool.

---

## 🐍 Python: Ruff (Formatting & Imports)

### **Ruff** (Auto-fixes instantly)

❌ **Before** (Messy imports and single quotes)

```python
from odoo import models,fields
import os
from odoo import api

class MyModel(models.Model):
    _name='my.model'
    def my_method(self):
        return { 'status':'ok' }
```

✅ **After** (Sorted, standardized, and clean)

```python
import os

from odoo import api, fields, models


class MyModel(models.Model):
    _name = "my.model"

    def my_method(self):
        return {"status": "ok"}
```

---

## 🔍 Odoo Logic: Pylint-Odoo

### **1. Print Used** (W8116)

❌ **Before**

```python
def action_confirm(self):
    print("Confirming order")  # ❌ Blocks commit
```

✅ **After**

```python
def action_confirm(self):
    _logger.info("Confirming order")
```

### **2. Odoo 18 Translation** (W8161)

❌ **Before**

```python
from odoo import _
msg = _("Hello")
```

✅ **After**

```python
msg = self.env._("Hello")  # ✅ Preferred in Odoo 18
```

---

## ✨ XML Views: Prettier & OCA Checks

### **Prettier** (Auto-fixes indentation)

❌ **Before**

```xml
<record id="my_view" model="ir.ui.view">
<field name="name">view</field>
<field name="arch" type="xml">
<form><group><field name="name"/></group></form>
</field></record>
```

✅ **After**

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<record id="my_view" model="ir.ui.view">
    <field name="name">view</field>
    <field name="arch" type="xml">
        <form>
            <group>
                <field name="name" />
            </group>
        </form>
    </field>
</record>
```

### **Redundant Module Name** (xml-id-redundant)

❌ **Before** (Module is `my_module`)

```xml
<record id="my_module.my_record_id" model="...">
```

✅ **After** (Cleaner)

```xml
<record id="my_record_id" model="...">
```

---

## 📦 Manifest & Repository

### **Superfluous Keys** (C8116)

❌ **Before**

```python
{
    "name": "Module",
    "installable": True,  # ❌ Default
    "data": [],           # ❌ Default
}
```

✅ **After**

```python
{
    "name": "Module",
}
```

### **Maintainer Tools (Website Fix)**

❌ **Before**

```python
"website": "http://my-old-site.com",
```

✅ **After** (Auto-fixed to your repo URL)

```python
"website": "https://github.com/nada-adel-mohamed/python-precommit-demo",
```

---

## 🌍 Translations (.po files)

### **PO Checks** (po-python-parse)

❌ **Before**

```po
msgid "Hello %s"
msgstr "Bonjour"  # ❌ Error: Missing %s in translation
```

✅ **After**

```po
msgid "Hello %s"
msgstr "Bonjour %s"
```

---

## 🛠️ General File Cleanup

### **1. Debug Statements**

❌ **Before**

```python
import pdb; pdb.set_trace()  # ❌ STOPS the commit
```

✅ **After**

```python
# (Remove the line completely before committing)
```

### **2. Mixed Line Endings**

❌ **Before** (Windows style CRLF)
`Line 1 \r\n`
`Line 2 \r\n`

✅ **After** (Fixed to Linux style LF)
`Line 1 \n`
`Line 2 \n`

### **3. Trailing Whitespace**

❌ **Before**

```python
x = 10      # [space][space][space]
```

✅ **After**

```python
x = 10
```

---

### 💡 Remember:

If the commit fails with **"files were modified by this hook"**, just run:

1. `git add .`
2. `git commit -m "..."`
   The tools already did the work for you!
