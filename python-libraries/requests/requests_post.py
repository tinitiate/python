## Pre-requiste for the code to run 
#  pip install requests

import requests
import json

# Define the URL to send the request to
url = "https://fakestoreapi.com/products"

# Define the data to send in the request body
data = {
    "title": "test product",
    "price": 13.5,
    "description": "lorem ipsum set",
    "image": "https://i.pravatar.cc",
    "category": "electronic"
}

# Define any headers to include in the request
headers = {"Content-Type": "application/json"}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))
json_response = response.json()

print(json_response)