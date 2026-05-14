import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VISUAL_CROSSING_API_KEY")
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"


def get_weather(city: str):

    url = f"{BASE_URL}/{city}?unitGroup=metric&key={API_KEY}&contentType=json"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "city": city,
            "temperature": data["currentConditions"]["temp"],
            "humidity": data["currentConditions"]["humidity"],
            "conditions": data["currentConditions"]["conditions"]
        }

    except Exception:
        return None