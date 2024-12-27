# OAuth Notes

## What is an OAuth Grant?

- The way the client requests an auth token.

---

## Research and Vulnerabilities

- Understand the structure of the app.
- Research misconfigurations from the docs.

---

## Key Points

- There is a lot to cover:
  - Chaining vulnerabilities is important in leaking auth tokens.
  - You can send the URL of a page with HTML injection because Firefox sends the URL in the `Referer` header.

---

## Standard OAuth Service Provider Endpoints

- `/.well-known/openid-configuration`
- `/.well-known/oauth-authorization-server`
