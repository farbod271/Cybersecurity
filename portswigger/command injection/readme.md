# Injection Techniques

This section covers various ways to inject code and execute commands, which can lead to vulnerabilities in an application.

## Key Injection Methods

- **Basic Injection Operators**:
  - `&`  
  - `&&`  
  - `|`  
  - `||`

- **Time-Based Injection**: This technique involves delays to detect successful injections based on response time.

- **Saving to Static Folders**: Injecting payloads that write to static folders can be useful for persistence.

- **DNS Lookup**: You can use `nslookup` to trigger a DNS request to your server. For example:  
This triggers a DNS lookup to the attacker's domain, sending the result of the `whoami` command.

- **Inline Command Injection**: Using backticks (\`) or `$()` allows for inline command injection, which lets you execute commands within the current context.

- **Context Management**: If injection occurs within double quotes (`"`) or single quotes (`'`), you need to properly terminate the context to execute the command.

- **Mass Testing**: A good strategy for mass testing is executing a simple `echo` command and checking the response to see if it contains specific words, as this can confirm whether injection is possible.
