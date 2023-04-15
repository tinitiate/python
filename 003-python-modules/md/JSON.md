# JSON 

* The Python json module provides a simple and easy-to-use API for working with JSON data.
*  JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate.
* The json module can be used to:
  - Decode JSON data from a string or file object.
  - Encode Python objects to JSON data.
  - Write JSON data to a file.
  - Read JSON data from a file.

## json.loads()

* Used to deserialize JSON formatted data into Python objects.
* This method reads JSON formatted data from a string and returns a Python object.
* `json.loads()` reads data from a string.

```python
import json

# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)

# Get Subset of JSON
print(data["BillDetails"])

# JSON Nested value, Get First Product
print(data["BillDetails"][0]["Product"])

# JSON Get All Products
for restaurant in data["BillDetails"]:
    print(restaurant["Product"])
```

## json.dumps()

* Used to serialize Python objects into JSON formatted data.
* This method serializes a Python object and returns the resulting JSON formatted data as a string.
*  `json.dumps()` returns the serialized data as a string.

```python
import json

# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""
data = json.loads(bill_json)
for restaurant in data["BillDetails"]:
      del restaurant["Product"]
      data_new = json.dumps(data, indent=2)
      print(data_new)
```

## json.load()

* Used to deserialize JSON formatted data into Python objects.
* This method reads JSON formatted data from a file-like object and returns a Python object.
* `json.load()` reads data from a file-like object such as a file object*/dictionary* .

```python
import json
with open('E:\\python-master\\media\\003-python-modules\\bills.json') as f:
    data = json.load(f)
    print(data)

StoreLocation=data['StoreLocation']
BillDate=data['BillDate']

for bill in data['BillDetails']:
    Product=bill['Product']
    print(Product)

```

## json.dump()

* Used to serialize Python objects into JSON formatted data.
* This method serializes a Python object and writes the resulting JSON formatted data to a file-like object.
*  `json.dump()` writes the serialized data to a file-like object such as a file object.

```python
import json

# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""
data = json.loads(bill_json)
for restaurant in data["BillDetails"]:
      del restaurant["Product"]
    #   data_new = json.dumps(data, indent=2)
    
with open('E:\\python-master\\media\\003-python-modules\\Bills_new.json', 'w') as f:
    json.dump(data, f, indent=2)
#  f.write(data_new)
```

