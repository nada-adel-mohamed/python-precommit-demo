# Odoo: PO Translation Files (oca-checks-po)

### What it does:

This hook manages and validates your Odoo translation files (found in the `i18n/` folder). It ensures they are formatted correctly and won't crash when Odoo tries to load them.

### Key Checks:

1. **Duplicate IDs:** Ensures you don't have the same translation ID twice in one file.
2. **Formatting:** Checks that lines are wrapped at 78 columns (standard) and sorted alphabetically.
3. **Variables:** Ensures that if the original text has `%s` (a placeholder), the translated text also has it.

### Example ❌ (Broken PO)

```po
# No module comment
msgid "Hello %s"
msgstr "مرحبا"  # Error: Missing the %s variable in the translation!
```

### Example ✅ (Correct PO)

```po
# module: my_module
msgid "Hello %s"
msgstr "مرحبا %s"  # Correct: Variable included
```

---

**How to fix:** Open the `.po` file in the `i18n/` folder and fix the syntax or missing variables.
