```python
import json
import requests

# Reading json file to json object/dictionary  
# Using Load

with open('bills.json') as f:    
    data = json.load(f)
    # print(data)

StoreLocation=data['StoreLocation']  
BillDate=data['BillDate']

for bill in data['BillDetails']:
    Product=bill['Product']
    print(Product)


# Using API
# Using Loads
request = requests.get("http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json")
response =request.text

data = json.loads(response)
print(json.dumps(data, indent=2))

dataseries=list()
temp=dict()

for item in data['dataseries']:
    temp['timepoint'] = item['timepoint']
    temp['cloudcover'] = item['cloudcover']
    temp['seeing'] = item['seeing']    
    temp['transparency'] = item['transparency']
    temp['rh2m'] = item['rh2m']
    temp['lifted_index'] = item['lifted_index']
    temp['lifted_index'] = item['lifted_index']
    
    dataseries.append({
        'Timepoint':temp['timepoint'],
        'Cloudcover': temp['cloudcover'],
        'Seeing': temp['seeing'],
        'Sransparency': temp['transparency'],
        'Rh2m': temp['rh2m'],
        'Lifted_index': temp['lifted_index']
    })     
    
with open('Weather_forecasts.json', 'w') as f:
  json.dump(dataseries, f, indent=2)
```


