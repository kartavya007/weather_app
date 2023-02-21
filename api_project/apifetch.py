import requests
import json
# param = 
def fetch_current(query) -> dict:
    key = "<Your_API_Key>"
    response_API = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={query}")
    data = response_API.text
    data = json.loads(response_API.text)
    return data
def fetch_forecast(query , day):
    key = "<Your_API_Key>"
    response_API = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={query}&days={day}")
    data = json.loads(response_API.text)
    for i in data :
        print(i)
if __name__ == "__main__":
    fetch_forecast()