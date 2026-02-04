# isort: The Import Sorter

### What it does:
Organizes your `import` statements at the top of the file. It groups them into:
1. Standard library imports (e.g., `os`, `sys`)
2. Third-party imports (libraries you installed)
3. Your own project imports

### Example ❌ (Bad Code)
```python
import sys
import os
from my_app import models
import datetime
```

### Example ✅ (After isort runs)
```python
import datetime
import os
import sys

from my_app import models
```

---
**How to fix:** isort fixes this **automatically** when you run `pre-commit`.
