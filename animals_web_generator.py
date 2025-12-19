from dotenv import load_dotenv
import webbrowser
import os
import requests
import data_fetcher

# ---- CONFIG ----
load_dotenv()  # Looks for .env in current directory or parent dirs

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY is not set")

API_URL = "https://api.api-ninjas.com/v1/animals"
TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"


def serialize_animal(animal_obj):
    """serializing the animal"""

    name = animal_obj.get("name", "")
    locations = animal_obj.get("locations", [])
    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet", "")
    type_ = characteristics.get("type", "")

    location_text = ", ".join(locations) if isinstance(locations, list) else locations

    html = '<li class="cards__item">\n'
    html += f'  <div class="card__title">{name}</div>\n'
    html += '  <p class="card__text">\n'

    if diet:
        html += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location_text:
        html += f'      <strong>Location:</strong> {location_text}<br/>\n'
    if type_:
        html += f'      <strong>Type:</strong> {type_}<br/>\n'

    html += '  </p>\n'
    html += '</li>\n'

    return html


def main():
    # 1. Ask the user for an animal name
    query = input("Enter a name of an animal: ")

    if not query:
        print("Error: You must enter a valid animal name.")
        return

    # 2. Fetch results from API
    # initializing the Variable
    animals_data = []

    try:
        animals_data = data_fetcher.fetch_data(query)
    except Exception as e:
        print(f"Error by fetching {query}: {e}")

    if not animals_data:
        animals_info = f'<h2>The animal "{query}" doesn\'t exist.</h2>'
        #print("No animals found.")
        return


    # 3. Build HTML items
    animals_info = ""
    for animal in animals_data:
        animals_info += serialize_animal(animal)

    # 4. Load template
    try:
        with open(TEMPLATE_FILE, "r") as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Template file '{TEMPLATE_FILE}' not found.")
        return

    # 5. Insert the animal info
    output_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    # 6. Write result file
    with open(OUTPUT_FILE, "w") as f:
        f.write(output_html)

    print(f"Website was successfully generated to the file {OUTPUT_FILE}.")

    # 7. Open in browser
    webbrowser.open("file://" + os.path.abspath(OUTPUT_FILE))


if __name__ == "__main__":
    main()
