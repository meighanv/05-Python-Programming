import requests

url = 'http://www.py4inf.com/code/romeo-full.txt'

r = requests.get(url)
print(r.text[0:3000])