def fetch_data():
"""fetching the animal data via API call"""
URL = https://api.api-ninjas.com/v1/animals
    try:
        response = requests.get(
            API_URL,

            headers={"X-Api-Key": API_KEY},
            params={"name": query}
        )
        response.raise_for_status()
        animals_data = response.json()