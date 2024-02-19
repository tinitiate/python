import json
import jsonschema

# read the JSON data from file
try:
    with open('E:/python-master/media/003-python-modules/product.json', 'r') as f:
        data = json.load(f)
except ValueError as e:
    print("Malformed JSON data:", e)
    exit()

# read the JSON schema from file
try:
    with open('E:/python-master/media/003-python-modules/schema.json', 'r') as f:
        schema = json.load(f)
except ValueError as e:
    print("Malformed JSON schema:", e)
    exit()

# validate the JSON data against the schema
try:
    jsonschema.validate(data, schema)
    print("JSON data is valid!")
    
except jsonschema.exceptions.ValidationError as e:
    print("JSON validation error:", e)
    
