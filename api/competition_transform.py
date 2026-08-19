import json
import pandas as pd


JSON_FILE = "data/raw/competitions_sample.json"


def load_data():

    with open(
        JSON_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data


def extract_competitions(data):

    competitions = []

    for item in data["competitions"]:

        competition = {
            "competition_id": item["id"],
            "competition_name": item["name"],
            "parent_id": item["parent_id"],
            "type": item["type"],
            "gender": item["gender"],
            "category_id": item["category"]["id"]
        }

        competitions.append(competition)

    return competitions


def create_competition_dataframe(competitions):

    df = pd.DataFrame(competitions)

    return df


def extract_categories(data):

    categories = []

    for item in data["competitions"]:

        category = {
            "category_id": item["category"]["id"],
            "category_name": item["category"]["name"]
        }

        categories.append(category)

    return categories


def create_category_dataframe(categories):

    df = pd.DataFrame(categories)

    return df


if __name__ == "__main__":

    data = load_data()

    # Extract competitions
    competitions = extract_competitions(data)

    competitions_df = create_competition_dataframe(
        competitions
    )

    # Extract categories
    categories = extract_categories(data)

    categories_df = create_category_dataframe(
        categories
    )

    print("\nCompetition Data:")
    print(competitions_df)

    print("\nCategory Data:")
    print(categories_df)