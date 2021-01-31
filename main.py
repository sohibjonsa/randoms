import requests
from pprint import pprint

h = {'X-Api-Key':'e25bd86b47974b12b7b6e50253b2d628'}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=h)
data = r.json()

pprint(data)