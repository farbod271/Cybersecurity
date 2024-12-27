## How Web Servers Handle File Uploads

Web servers often use the `filename` field in `multipart/form-data` requests to determine:
- The **name** of the uploaded file.
- The **location** where the file should be saved.

---

## Common Bypass Techniques

### 1. Upload Files to Another Directory
- Exploit poor directory validation to upload files to unintended or restricted directories.

### 2. Use `.htaccess` Files to Change Server Behavior
- Upload a `.htaccess` file to modify server configurations within the directory.
- Example: Whitelist `.txt` files but process them as PHP scripts.

#### `.htaccess` Example:
```apache
AddType application/x-httpd-php .txt
