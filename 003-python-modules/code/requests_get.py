import requests

response = requests.get('https://fakestoreapi.com/products')

print(response.text)

## Parameters 

l_params = {
    'limit': 3,
    'sort': 'desc'
}

response = requests.get('https://fakestoreapi.com/products', params=l_params)
json_data = response.json()
print(json_data)


