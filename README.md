# 🌦 Weather API (FastAPI + Redis Cache)

A simple Weather API built with FastAPI that fetches real-time weather data and uses Redis caching to improve performance and reduce API calls.



## Features

- Get current weather by city name
- Redis caching for fast responses
- Cache expiration tracking (TTL)
- External weather API integration (Visual Crossing)
- Proper error handling (invalid city, API failure, server issues)
- Clean modular backend structure



## Tech Stack

- Python
- FastAPI
- Redis
- Requests
- Visual Crossing Weather API

### 1. Clone the repository

git clone https://github.com/47Doings/weather-api.git
cd weather-api



### 2. Create virtual environment

python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate



### 3. Install dependencies

pip install -r requirements.txt



## Environment Variables

Create a `.env` file in the root folder:

VISUAL_CROSSING_API_KEY=your_api_key
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port
REDIS_PASSWORD=your_redis_password



## Run the project

uvicorn main:app --reload

Then open:

http://127.0.0.1:8000/weather/Accra



## Example API Response

{
  "success": true,
  "source": "cache",
  "data": {
    "city": "accra",
    "temperature": 30,
    "humidity": 74.6,
    "conditions": "Partially cloudy"
  }
}



## What I Learned

- Building REST APIs with FastAPI
- Working with external APIs
- Using Redis for caching
- Backend error handling
- Git & GitHub workflow



## Future Improvements

- Forecast endpoint (7-day weather)
- Rate limiting system
- Search history tracking (Redis lists)
- Docker containerization
- Cloud deployment (Render / Railway)


