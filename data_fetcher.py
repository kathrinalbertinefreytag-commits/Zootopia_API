import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")

def fetch_data(query: str):
    """Fetch animal data via API call from API Ninjas."""
    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": query}
        )
        response.raise_for_status()
        animals_data = response.json()
        return animals_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
