import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')


def get_coordinates(city_name: str):
    try:
        response = requests.get(
            'https://api.openweathermap.org/geo/1.0/direct',
            params={'q': city_name, 'limit': 1, 'appid': API_KEY},
            timeout=5
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

    data = response.json()
    if not data:
        return None, None
    city_data = data[0]
    return city_data['lat'], city_data['lon']
