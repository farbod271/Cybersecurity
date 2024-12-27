### 1. API Testing Overview
API testing involves:
- **API Recon:** Identifying API endpoints and resources.
- **Parameter Acceptance:** Determining how the API processes input parameters and supported content types.
- **HTTP Method Acceptance:** Testing the API's response to different HTTP methods (e.g., GET, POST, PATCH).
- **Rate Limiting and Authentication:** Verifying the implementation of rate limits and authentication mechanisms.

---

### 2. API Recon
- **Check the Root Link:** Start with the base URL to discover potential endpoints.
- **JavaScript Files:** Investigate JavaScript files for hardcoded endpoints or hidden API paths.
- **Machine-Readable Documentation:** Tools like Postman and SoapUI can help parse machine-readable API documentation formats such as OpenAPI.

---

### 3. HTTP Methods
- Use Burp Intruder's built-in HTTP verbs list to automate testing with various HTTP methods.
- Example practice:
  - Change `GET` requests to `PATCH` and observe responses.
  - Always check `/api` paths for exposed endpoints.

---

### 4. Parameter Handling
Different frameworks handle duplicate parameters differently:
- **PHP:** Parses only the last parameter.
  - Example: Searching for `?user=peter&user=carlos` would result in `user=carlos`.
- **ASP.NET:** Combines all parameters.
  - Example: Searching for `?user=peter&user=carlos` might result in `user=peter,carlos`, which could trigger an "Invalid username" error.
- **Node.js/Express:** Parses only the first parameter.
  - Example: Searching for `?user=peter&user=carlos` would result in `user=peter`.

---

### 5. API Documentation Paths
API documentation is often available at:
- `/api`
- `/swagger/index.html`
- `/openapi.json`

---
