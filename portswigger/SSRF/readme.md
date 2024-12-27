# SSRF (Server-Side Request Forgery) Notes

## Techniques

1. **Alternative IP Representations**:
   - Use alternative representations for `127.0.0.1`, such as:
     - `2130706433`
     - `017700000001`
     - `127.1`

2. **Registering a Custom Domain**:
   - Register a domain name that resolves to `127.0.0.1`.
   - Example: Use `spoofed.burpcollaborator.net`.

3. **Obfuscation**:
   - Obfuscate blocked strings using:
     - URL encoding.
     - Case variation.

4. **Controlled URL Redirects**:
   - Provide a URL under your control that redirects to the target URL.
   - Try different techniques:
     - Use different HTTP redirect codes.
     - Switch protocols (e.g., from `http:` to `https:`).

---

## Using Open Redirects for SSRF

### Concept
- If you find an open redirect, and the server makes requests to a URL containing that redirect, you can exploit it for SSRF.

### Example
- Stock API Example:


---

## Lesson Learned

- If the URL has basic authentication enabled, check for SSRF and whitelist bypasses:
- Example:
  ```
  http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos
  ```
  - Here, `#` is double URL-encoded.

---

## Transferring Information via `nslookup`

### Technique
- Add the data as a subdomain and perform `nslookup` on your server.
- Example:
  ```
  some-data.yourserver.com
  ```
