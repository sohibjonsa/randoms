import requests
from pprint import pprint

h = {'X-Api-Key':'b06977ffaecb493691a2057adb2671d9'}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=h)
data = r.json()
pprint(data)