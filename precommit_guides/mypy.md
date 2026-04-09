# mypy: The Static Type Checker

### What it does:

Checks your Python "Type Hints" to make sure you aren't passing the wrong kind of data to a function.

### Example ❌ (Bad Code)

```python
def greet(name: str):
    print("Hello " + name)

# This will fail! You passed a number instead of a string.
greet(123)
```

### Example ✅ (Correct Code)

```python
def greet(name: str):
    print("Hello " + name)

greet("Nada")
```

---

**How to fix:** Fix the data type or the function definition. This prevents the app from crashing later.
