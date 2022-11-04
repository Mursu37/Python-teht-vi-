import requests

API_KEY = "ea35448e40d905f795f4032207f7befb"
city = input("Anna kaupungin nimi: ")
geocode = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}"
geo_data = requests.get(geocode).json()

try:
    city_name = geo_data[0]["local_names"]["fi"]
except KeyError:
    city_name = geo_data[0]["name"]

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]
dsa = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=fi"
weather_data = requests.get(dsa).json()
print(f'Kaupunki: {city_name}'
      f'\n{weather_data["weather"][0]["description"]}'
      f'\n{weather_data["main"]["temp"]} astetta')
