import requests
response = requests.get('https://github.com/wadeChriestenson')
header = response.headers
for x in header:
    print(x, ':', header[x])
