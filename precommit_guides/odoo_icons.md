# Odoo: Icon Size Check

### What it does:
Ensures that your module icon (located at `static/description/icon.png`) is the correct size for the Odoo interface.

### The Rule:
- **Size:** Must be exactly **128 x 128 pixels**.
- **Format:** Usually **PNG**.

### Why?
If the icon is too large (e.g., 500x500), it makes your module list load slowly. If it's too small, it looks blurry.

---
**How to fix:** Open your `icon.png` in an image editor (like Photoshop, GIMP, or Paint) and resize it to exactly 128x128.
