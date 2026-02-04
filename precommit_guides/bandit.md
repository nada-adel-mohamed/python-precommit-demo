# Bandit: The Security Guard

### What it does:
Scans your code for security vulnerabilities like hardcoded passwords or dangerous shell commands.

### Example ❌ (Bad Code)
```python
# Hardcoded password
password = "admin123"

# Dangerous command (String injection)
subprocess.run("rm " + user_input, shell=True)
```

### Example ✅ (Secure Code)
```python
import os
# Use environment variables
password = os.getenv("DB_PASSWORD")

# Use Lists for shell commands
subprocess.run(["rm", user_input])
```

---
**How to fix:** This is a **High Criticality** error. You must fix your logic before you can commit.
