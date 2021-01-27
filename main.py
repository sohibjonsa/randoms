import requests

h = {'X-Api-Key':'b06977ffaecb493691a2057adb2671d9'}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=h)
print(r.url)