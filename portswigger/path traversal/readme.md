# File Traversal Notes

## Goal

- The primary target is to access sensitive files:
  - In Linux: `/etc/passwd`
  - In Windows: `windows\win.ini`

---

## Bypass Techniques

### 1. Stripping Inner Input
- If the input is stripped from the inner side, a bypass can be:
  - `....//`

### 2. Encoding Techniques
- Use URL or double URL encoding for traversal:
  - Example: `%2e%2e%2f` translates to `../`

### 3. Base Directory Checks
- Some applications verify if the base directory is as expected.
- Test for ways to bypass this check.

### 4. Extension Validation
- If the app checks for specific file extensions, use a null byte to terminate the filename:
  - Example: `filename=../../../etc/passwd%00.png`

---

## That's It!
