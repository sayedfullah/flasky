from dotenv import  load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Durban"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    weather_response = requests.get(request_url)
    return weather_response.json()

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\n Enter the name of the city: ")

    if not bool(city.strip()): 
        city = "Durban"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(get_current_weather())
