## HTTP Methods and Diagnostic Responses

### TRACE Method
- The HTTP TRACE method can be used to receive diagnostic responses from the server.
- Often used to debug requests but can expose sensitive information if misconfigured.

---

## Exposing Vulnerabilities

### Fuzzing Parameters
- **Description**: Vulnerabilities can be exposed by sending unexpected input to parameters.
- **Examples**:
  - Send a string instead of an integer to trigger an error.
  - Test for edge cases and improper input validation.

### Useful Files to Check
- `/sitemap.xml` and `/robots.txt`:
  - Often reveal paths that can be explored further.
- Source Code Exposure:
  - Modify file extensions (e.g., `.php` → `.txt`) to view the source code.
  - Use the `~` suffix or backups to locate unintended file versions.

### Hidden Directories
- Common examples include:
  - `/.git` directory: May expose sensitive project data.
  - `cgi-bin/phpinfo.php`: Displays PHP configuration information.

---

## Burp Suite Tips

### Engagement Tools
- Burp's engagement tools are invaluable for exploring and identifying vulnerabilities efficiently.

### Match and Replace
- Use Burp’s **Match and Replace** feature:
  - Modify HTTP headers on the fly.
  - Example: Add custom headers directly through your browser via Burp.

---

## Practical Example: Header Manipulation

### HTTP HEAD Method Example
- During a lab test, the `HEAD` method revealed the following header:
  ```http
  X-Custom-Ip-Authorization: 127.0.0.1
