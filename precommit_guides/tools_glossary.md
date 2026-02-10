# Odoo 18 Pre-commit: Tools Glossary

This document provides a quick reference for every tool included in your new Odoo 18 Gold Standard environment.

---

## 🐍 Python & Odoo Logic

### **Ruff** (The Speed Demon)

- **What it does:** Replaces Black, Isort, and Flake8.
- **Feature:** Automatically formats Python code, sorts imports, and removes unused variables/imports. It is nearly 100x faster than the tools it replaces.
- **Fixes itself?** Yes.

### **Pylint-Odoo** (The Inspector)

- **What it does:** Deep analysis of Odoo-specific code.
- **Feature:** Catches SQL injection, translation misuse (`_()`), and ensures you use Odoo 18 APIs correctly (like `self.env._`).
- **Fixes itself?** No (Manual fix required).

### **oca-checks-odoo-module** (The Architect)

- **What it does:** Validates the structure of your module.
- **Feature:** Ensures XML IDs are unique across files and CSV data files are formatted correctly.
- **Fixes itself?** Partial.

---

## ✨ Formatting & Style

### **Prettier + plugin-xml** (The Polisher)

- **What it does:** Formats XML, SCSS, JS, and YAML.
- **Feature:** Specifically designed to make Odoo views (XML) look perfect with consistent indentation and attribute ordering.
- **Fixes itself?** Yes.

### **ESLint** (The JS Guard)

- **What it does:** Checks your JavaScript (Owl) logic.
- **Feature:** Catches common JS errors and ensures your scripts follow modern standards.
- **Fixes itself?** Yes (most issues).

---

## 📦 OCA Repository Management

### **Whool** (The Clerk)

- **What it does:** Manages module packaging.
- **Feature:** Standardizes manifest versioning and prepares modules for publication to the OCA app store.
- **Fixes itself?** Yes.

### **oca-gen-addon-readme** (The Writer)

- **What it does:** Builds your `README.rst`.
- **Feature:** Dynamically generates a professional documentation file by combining small text fragments (Description, Usage, Credits).
- **Fixes itself?** Yes.

### **oca-fix-manifest-website** (The Linker)

- **What it does:** Auto-checks your manifest's website link.
- **Feature:** Ensures the URL points to the correct GitHub repository.
- **Fixes itself?** Yes.

---

## 🛠️ General Quality (Standard Hooks)

### **trailing-whitespace**

- **Action:** Deletes extra spaces at the end of lines.

### **end-of-file-fixer**

- **Action:** Ensures every file ends with a single blank line.

### **mixed-line-ending**

- **Action:** Forces all files to use Linux-style (LF) line endings—mandatory for OCA repositories.

### **debug-statements**

- **Action:** Blocks the commit if you accidentally leave a `breakpoint()` or `pdb.set_trace()` in your code.

### **check-merge-conflict**

- **Action:** Prevents you from committing files that still have merge conflict markers (`<<<<<<< HEAD`).

---

## 🚦 How to use these tools?

Most of these tools run **automatically** when you commit. If a tool fails:

1.  **Check the output:** It will often say "files were modified by this hook".
2.  **Staging:** Run `git add .` to accept the auto-fixes.
3.  **Commit:** Run `git commit` again.
