# Flake8: The Style Police

### What it does:

Finds logic errors, unused variables, and PEP 8 style violations that automatic formatters can't fix.

### Example ❌ (Bad Code)

```python
import os # Error: Unused import

def calculate():
    x = 10 # Error: Variable assigned but never used
    return 5
```

### Example ✅ (Correct Code)

```python
def calculate():
    return 5
```

---

**How to fix:** Flake8 **cannot fix this for you**. It will block your commit and tell you the line number to fix manually.
