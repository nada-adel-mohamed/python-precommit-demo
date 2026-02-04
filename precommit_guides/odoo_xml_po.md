# Odoo: XML & PO Validator

### What it does:
Odoo relies heavily on XML for views and PO files for translations. This hook ensures these files are not broken.

### Example ❌ (Bad XML)
```xml
<record id="my_view" model="ir.ui.view">
    <field name="name">my.view</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name">   <!-- Error: Never closed this tag! -->
        </tree>
    </field>
</record>
```

### Example ✅ (Correct XML)
```xml
<record id="my_view" model="ir.ui.view">
    <field name="name">my.view</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <tree>
            <field name="name"/>
        </tree>
    </field>
</record>
```

---
**How to fix:** Check the file mentioned in the error log and fix the broken XML syntax.
