# Black: The Code Formatter

### What it does:

Black is "The Uncompromising Code Formatter." It automatically rewrites your code to be beautiful and easy to read. It handles spacing, indentation, and line lengths.

### Example ❌ (Bad Code)

```python
def my_function( a,b):
    x={ 'name':'nada','age':25}
    print("Hello"   )
    return a+b
```

### Example ✅ (After Black runs)

```python
def my_function(a, b):
    x = {"name": "nada", "age": 25}
    print("Hello")
    return a + b
```

---

**How to fix:** Black fixes this **automatically** when you run `pre-commit`.
