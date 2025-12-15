from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY").strip()

url = "https://api.api-ninjas.com/v1/animals"

response = requests.get(
    url,
    headers={
        "X-Api-Key": API_KEY,
        "User-Agent": "Mozilla/5.0"
    },
    params={"name": "elephant"}
)

print("Status:", response.status_code)
print("Text:", response.text)
