# Requests library 

* The Requests library is a popular library in Python for making HTTP requests.
*  HTTP request methods available in the library (such as `requests.get()`, `requests.post()`,`requests.put()`, `requests.delete()`, etc.).
* It abstracts the complexities of making requests behind a simple API, allowing you to send HTTP/1.1 requests with python.
* `response.text`: This returns the response content in Unicode (i.e., the text of the response).
* `response.content`: This returns the raw bytes of the response.
* `response.json()`: This method returns the response content parsed as a JSON object.
* `response.status_code`: This returns the HTTP status code of the response (e.g., 200, 404, 500, etc.).
* `response.headers`: This returns a dictionary of the response headers.
* `response.raise_for_status()`: This method raises an HTTP Error if the response status code indicates a client error (4xx) or server error (5xx).

## Installing Requests

* Before using the Requests library, we need to install it.

* We can do this using pip, a package manager for Python:

  ```shell
  pip install requests
  ```

  

## Making a GET Request

* The `get` method sends an HTTP GET request to the specified URL and returns a `Response` object. 

  ```python
  import requests
  
  response = requests.get('https://fakestoreapi.com/products')
  
  print(response.text)
  
  ```

* The `text` attribute of the `Response` object contains the response body as a string.

### Passing Parameters

* We can pass parameters with a GET request by adding them to the URL.

* `params` dictionary contains the query string parameters that will be appended to the URL. 

* The `requests.get()` function takes this dictionary as an argument in the `params` parameter. 

* Here are the most commonly used used parameters for the `requests.get()` method:

  - `url` (required): A string representing the URL to which the GET request will be made.
  
  - `params` (optional): A dictionary, list of tuples or bytes to send in the query string for the request.
  
  - `headers` (optional): A dictionary containing HTTP headers to include in the request.
  
  - `cookies` (optional): A dictionary or `RequestsCookieJar` containing cookies to include in the request.
  
  - `auth` (optional): A tuple of `username` and `password` for HTTP authentication.
  
  - `timeout` (optional): A float or tuple representing the number of seconds to wait for a response.
  
  - `allow_redirects` (optional): A Boolean value indicating whether or not to follow redirects.
  
  - `proxies` (optional): A dictionary containing the proxy URL to use for the request.
  
  - `verify` (optional): A Boolean value indicating whether or not to verify SSL certificates.
  
  - `stream` (optional): A Boolean value indicating whether or not to stream the response content.
  
    ```python
    import requests
    
    params = {
        'limit': 3,
        'sort': 'desc'
    }
    response = requests.get('https://fakestoreapi.com/products', params=params)
    json_data = response.json()
    print(json_data)
    
    ```
  
    

## POST

* The `requests.post()` method is a function from the `requests` library in Python, used for making HTTP POST requests to a specified URL.

* Here are the most commonly used parameters for the `requests.post()` method:

  - `url` (required): A string representing the URL to which the POST request will be made.

  - `data` (optional): A dictionary, list of tuples, or bytes to send in the body of the request.

  - `json` (optional): A JSON serializable object to be included in the body of the request as JSON.

  - `headers` (optional): A dictionary containing HTTP headers to include in the request.

  - `cookies` (optional): A dictionary or `RequestsCookieJar` containing cookies to include in the request.

  - `auth` (optional): A tuple of `username` and `password` for HTTP authentication.

  - `timeout` (optional): A float or tuple representing the number of seconds to wait for a response.

  - `allow_redirects` (optional): A Boolean value indicating whether or not to follow redirects.

  - `proxies` (optional): A dictionary containing the proxy URL to use for the request.

  - `verify` (optional): A Boolean value indicating whether or not to verify SSL certificates.

  - `stream` (optional): A Boolean value indicating whether or not to stream the response content.

    ```python
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
    ```

* `headers = {"Content-Type": "application/json"}` - This sets the `Content-Type` header of the HTTP request to indicate that we're sending JSON data.

## Put

* The `requests.put()` method is a function from the `requests` library in Python, used for making HTTP PUT requests to a specified URL.

* The `Put` method is used to update or replace an existing resource with new data.

* Here are the most commonly used parameters for the `requests.put()` method in Python:

  - `url` (required): A string representing the URL to which the PUT request will be made.

  - `data` (optional): A dictionary, list of tuples, or bytes to send in the body of the request.

  - `headers` (optional): A dictionary containing HTTP headers to include in the request.

  - `cookies` (optional): A dictionary or `RequestsCookieJar` containing cookies to include in the request.

  - `auth` (optional): A tuple of `username` and `password` for HTTP authentication.

  - `timeout` (optional): A float or tuple representing the number of seconds to wait for a response.

  - `allow_redirects` (optional): A Boolean value indicating whether or not to follow redirects.

  - `proxies` (optional): A dictionary containing the proxy URL to use for the request.

  - `verify` (optional): A Boolean value indicating whether or not to verify SSL certificates.

  - `stream` (optional): A Boolean value indicating whether or not to stream the response content.

    ```python
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
    ```

    

## Delete 

* The `requests.delete()` method is a function from the `requests` library in Python, used for making HTTP DELETE requests to a specified URL.

* The `requests.delete()` method in Python accepts the following commonly used parameters:

  - `url` (required): A string representing the URL to which the DELETE request will be made.

  - `headers` (optional): A dictionary containing HTTP headers to include in the request.

  - `cookies` (optional): A dictionary or `RequestsCookieJar` containing cookies to include in the request.

  - `auth` (optional): A tuple of `username` and `password` for HTTP authentication.

  - `timeout` (optional): A float or tuple representing the number of seconds to wait for a response.

  - `allow_redirects` (optional): A Boolean value indicating whether or not to follow redirects.

  - `proxies` (optional): A dictionary containing the proxy URL to use for the request.

  - `verify` (optional): A Boolean value indicating whether or not to verify SSL certificates.

  - `stream` (optional): A Boolean value indicating whether or not to stream the response content.

  - `params` (optional): A dictionary containing key-value pairs to send in the query string of the URL.

    ```python
    import requests
    
    url = 'https://fakestoreapi.com/products/8'
    response = requests.delete(url)
    
    if response.status_code == 200:
        print('DELETE request successful!')
    else:
        print('DELETE request failed with status code:', response.status_code)
    ```

    

  

