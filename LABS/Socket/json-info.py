import json
import requests 
url = 'https://analytics.usa.gov/data/live/realtime.json'
r = requests.get(url)
data = r.json()
users = (data['data'][0])
for key, value in users.items():
    print(f'{key}: {value}')
    

