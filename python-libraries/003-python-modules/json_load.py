import json

# ###########################################
# Reading json file to json object/dictionary  
# Using Load
# ###########################################
with open('E:\\python-master\\media\\003-python-modules\\bills.json') as f:
    data = json.load(f)
    print(data)

StoreLocation=data['StoreLocation']
print(StoreLocation)

for bill in data['BillDetails']:
    Product=bill['Product']
    print(Product)
