import requests
from urllib.parse import quote

url = 'https://0a82005204bfe2b49093d5b300f90069.web-security-academy.net/product/stock'

#open a txt file and read each line for payload

with open('attacks.txt', 'r') as file:
    payloads = file.readlines()


# for payload in payloads:
# payload = payload.strip()
# payload = quote(payload)
response = requests.post(url, data={'stockApi': f'https://stock.weliketoshop.net'}, cookies={'session': "skJ58DjczVdtD8BZeTUUtI4Q9oqEOzMo"})
print( response.status_code)
# if response.status_code == 200:
    # print(f'Found it! {payload}')
    # break


