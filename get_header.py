import requests
response = requests.get('https://www.wikipedia.com')
header = response.headers
for x in header:
    print(x, ':', header[x])
