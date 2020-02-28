""" MARKDOWN
---
Title: Python JSON
Tags: Python JSON, Read Json, write Json, Nested json
Author: Venkata Bhattaram |  www.github.com/tinitiate
ContentName: python-json
---
MARKDOWN """
""" MARKDOWN
# Python JSON Module
* JSON is a data format widely used in REST web services, It stands for 
  javascript Object Notation.
* Here we demonstrate the following
  * Read Simple JSON, nested JSON
  * Create JSON from Python
  * Convert JSON to Dictionary, Lists 

## Python Read JSON
* Here we demonstrate python program reading a String in JSON format
* **LOADS** Function parses JSON
MARKDOWN """
# MARKDOWN```python

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
y = json.loads(bill_json)

# Get Subset of JSON
print(y["BillDetails"])

# JSON Nested value, Get First Product
print(y["BillDetails"][0]["Product"])

# JSON Get All Products
for restaurant in y["BillDetails"]:
    print(restaurant["Product"])

# MARKDOWN```

