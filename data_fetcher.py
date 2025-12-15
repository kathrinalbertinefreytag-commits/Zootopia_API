from dotenv import load_dotenv
import requests
from pathlib import Path
import os

# to have the direct path to our .env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")

def fetch_data(query: str):
    """Fetch animal data via API call from API Ninjas."""
    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY.strip(), "User-Agent": "Mozilla/5.0"},

            params={"name": query.lower()}
        )
        response.raise_for_status()
        animals_data = response.json()
        return animals_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
