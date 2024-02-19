## Pre-requiste for the code to run 
#  pip install requests

import requests

url = 'https://fakestoreapi.com/products/8'
response = requests.delete(url)

if response.status_code == 200:
    print('DELETE request successful!')
else:
    print('DELETE request failed with status code:', response.status_code)