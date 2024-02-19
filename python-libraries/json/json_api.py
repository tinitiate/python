import json
import requests

# ###########################################
# Using API
# Using Loads
# ###########################################
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
    
with open('E:\\python-master\\media\\003-python-modules\\Weather_forecasts.json', 'w') as f:
  json.dump(dataseries, f, indent=2)