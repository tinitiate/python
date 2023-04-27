import requests
import json

def send_post_request_json(url, data):
    """
    Sends a POST request with json-encoded data to the specified URL
    Prints the response text received from the API endpoint
    """
    response = requests.post(url, data=data)
    print(response.text)

def send_post_request_json_with_headers(url, data, headers):
    """
    Sends a POST request with json-encoded data and headers to the specified URL
    Prints the response text received from the API endpoint
    """
    response = requests.post(url, json=data, headers=headers)
    print(response.text)

def main():
    # URL to API endpoint
    url = 'https://fakestoreapi.com/products'

    # JSON-encoded data to be sent in the request body
    data = {
        'title': 'Laptop',
        'price': 900.99,
        'description': 'Dell Inspiron',
        'image': 'https://i.pravatar.cc',
        'category': 'electronic'
    }

    # POST request with JSON-encoded data
    json_data = send_post_request_json(url, data)

    # Headers to be sent in the request
    headers = {'Content-Type': 'application/json'}

    # POST request with JSON-encoded data and headers
    json_data_with_headers = send_post_request_json_with_headers(url, data, headers)

if __name__ == '__main__':
    main()
