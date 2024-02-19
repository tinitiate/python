## Pre-requiste for the code to run 
#  pip install requests

import requests
import json

url = 'https://fakestoreapi.com/products/7'

data = {
    "title": "test product",
    "price": 13.5,
    "description": "lorem ipsum set",
    "image": "https://i.pravatar.cc",
    "category": "electronic"
}

headers = {"Content-Type": "application/json"}

response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print('PUT request successful!')
else:
    print('PUT request failed with status code:', response.status_code)

response_json = response.json()
print(response_json)