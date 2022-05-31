import requests
import arrow


# Get first hour of today
start = arrow.now().floor('day')

# Get last hour of today
end = arrow.now().ceil('day')

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
print(json_data)
