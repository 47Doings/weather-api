import redis 
import os 
from dotenv import load_dotenv

load_dotenv()

try:
    r = redis.Redis(
        host=os.getenv("REDIS_HOST"),
        port=os.getenv("REDIS_PORT"),
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=True
    )

    # Test connection
    r.set("test_key", "hello redis")
    value = r.get("test_key")

    print("Redis Connected Successfully ✔")
    print("Value:", value)

except Exception as e:
    print("Redis Connection Failed ❌")
    print(e)