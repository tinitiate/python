## Pre-requiste for the code to run 
#  pip install requests

import requests

response = requests.get('https://fakestoreapi.com/products')

print(response.text)
