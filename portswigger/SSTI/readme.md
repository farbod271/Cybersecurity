## Potential XSS and Server-Side Template Injection

The following code:

```js
render('Hello ' + username)
can sometimes be exploited for XSS and is often mistaken for a simple XSS vulnerability. However, by setting mathematical operations as the value of the parameter, we can test if this could also be a potential entry point for a server-side template injection attack.

example: ${{<%[%'"}}%
