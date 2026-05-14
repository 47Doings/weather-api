from fastapi import FastAPI
import json

from services.weather import get_weather
from services.cache import redis_client

app = FastAPI()

CACHE_EXPIRY = 60 * 60 * 12  # 12 hours


@app.get("/weather/{city}")
def weather(city: str):

    city = city.lower()

    # 1. Check cache
    cached = redis_client.get(city)

    if cached:
        return {
            "source": "cache",
            "data": json.loads(cached)
        }

    # 2. Call API
    weather_data = get_weather(city)

    if not weather_data:
        return {
            "error": "City not found or API error"
        }

    # 3. Save to cache
    redis_client.setex(
        city,
        CACHE_EXPIRY,
        json.dumps(weather_data)
    )

    # 4. Return response
    return {
        "source": "api",
        "data": weather_data
    }