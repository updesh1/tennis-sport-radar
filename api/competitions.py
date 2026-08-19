import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv


# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

API_KEY = os.getenv("SPORTRADAR_API_KEY")

if not API_KEY:
    raise ValueError(
        "SPORTRADAR_API_KEY not found. "
        "Please add it to your .env file."
    )


# --------------------------------------------------
# 2. API configuration
# --------------------------------------------------

BASE_URL = "https://api.sportradar.com/tennis/trial/v3/en"


# --------------------------------------------------
# 3. Create folders
# --------------------------------------------------

RAW_DATA_DIR = Path("data/raw")

RAW_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------------------------
# 4. Fetch competition data
# --------------------------------------------------

def fetch_competitions():
    """
    Fetch competition data from SportRadar API.
    """

    endpoint = f"{BASE_URL}/competitions.json"

    headers = {
        "accept": "application/json"
    }

    params = {
        "api_key": API_KEY
    }

    try:

        response = requests.get(
            endpoint,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        print("Competition data downloaded successfully.")

        return data

    except requests.exceptions.HTTPError as error:

        print("HTTP Error:", error)

    except requests.exceptions.ConnectionError:

        print("Connection Error: Could not connect to SportRadar.")

    except requests.exceptions.Timeout:

        print("Error: API request timed out.")

    except requests.exceptions.RequestException as error:

        print("Request Error:", error)

    return None


# --------------------------------------------------
# 5. Save raw JSON
# --------------------------------------------------

def save_raw_data(data):
    """
    Save original API response as JSON.
    """

    output_file = RAW_DATA_DIR / "competitions.json"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print(f"Raw data saved to: {output_file}")


# --------------------------------------------------
# 6. Main program
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("SPORTRADAR COMPETITION DATA EXTRACTION")
    print("=" * 50)

    competition_data = fetch_competitions()

    if competition_data:

        save_raw_data(competition_data)

        print("\nExtraction completed successfully.")

    else:

        print("\nNo data was retrieved.")