# Odoo: Manifest Checker

### What it does:

Validates your `__manifest__.py` file to ensure it follows Odoo's required format. It catches syntax errors and missing mandatory keys.

### Example ❌ (Bad Code)

```python
# __manifest__.py
{
    'name': 'My Module'
    'version': 1.0,  # Error 1: Missing comma after name, Error 2: Version must be a string '18.0.1.0.0'
    'depends': ['base']
}
```

### Example ✅ (Correct Code)

```python
# __manifest__.py
{
    'name': 'My Module',
    'version': '18.0.1.0.0',
    'category': 'Sales',
    'summary': 'A great module for Odoo 18',
    'depends': ['base'],
    'data': [
        'views/my_view.xml',
    ],
    'license': 'LGPL-3',
}
```

---

**How to fix:** Fix the syntax or missing keys in your `__manifest__.py`.
