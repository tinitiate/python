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



# json object to json string
for restaurant in data["BillDetails"]:
    # print(data)
    del restaurant["Product"]
    data_new =json.dumps(data)
    print(data_new)

# writing json string to json file.
with open('Bills_new.json', 'w') as f:
  json.dump(data_new, f, indent=2)

"""
# json object to JSON string with identation
# for restaurant in data["BillDetails"]:
      # del restaurant["Product"]
      # data_new = json.dumps(data, indent=2)
      # print(data_new)

# dumps object to JSON string with identation and sort
for restaurant in data["BillDetails"]:
    del restaurant["Product"]
    data_new = json.dumps(data, indent=2,sort_keys=True)
    print(data_new)
"""