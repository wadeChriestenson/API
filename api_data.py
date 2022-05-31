import requests
import arrow



response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 44.9429,
    'lng': 123.0351,
    'params': ','.join(['windSpeed', 'airTemperature']),
  },
  headers={
    'Authorization': '<your-stromglass_api_key>'
  }
)

# Do something with response data.
json_data = response.json()
print(response.headers)
print(json_data)
