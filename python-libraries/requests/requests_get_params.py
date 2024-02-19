## Pre-requiste for the code to run 
#  pip install requests

import requests
params = {
    'limit': 3,
    'sort': 'desc'
}
response = requests.get('https://fakestoreapi.com/products', params=params)
json_data = response.json()
print(json_data)