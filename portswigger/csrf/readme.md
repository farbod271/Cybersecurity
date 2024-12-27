# Security Concepts and Vulnerabilities

This section highlights some important security concepts and potential vulnerabilities to look out for.

## Key Points

- **SameSite and Same-Origin**: 
  - Review the meaning of SameSite and Same-Origin policies. SameSite cookies prevent cross-site request forgery (CSRF) attacks by restricting how cookies are sent with cross-site requests. Same-Origin includes the protocol, domain, and port.

- **SameSite=Lax Attribute**: Cookies set with `SameSite=Lax` are exempt from the two-minute window restriction.

- **eTLD**: The Effective Top-Level Domain (eTLD) applies when you have domains like `co.uk`. Even though it’s a subdomain, it’s treated as a separate domain.

- **Port and Subdomain**: Same-Origin policy also considers the port number and subdomains as part of the same origin.

- **Cookie Injection**: A clever technique to exploit cookies involves injecting `%0d%0a` (carriage return and line feed).

- **Open Redirects and CSRF**: Open redirects are useful for CSRF attacks. To find these vulnerabilities, look for the JavaScript file handling the redirection, as it's not always visible in Burp Suite.

- **Referer Header and CSRF**: In some cases, omitting the `Referer` header completely can bypass CSRF protections.
