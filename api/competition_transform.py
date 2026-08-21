import json
import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

JSON_FILE = "data/raw/competitions_sample.json"

COMPETITIONS_OUTPUT = "data/processed/competitions.csv"
CATEGORIES_OUTPUT = "data/processed/categories.csv"


# ============================================================
# STEP 1 — LOAD JSON DATA
# ============================================================

def load_data():

    with open(
        JSON_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return data


# ============================================================
# STEP 2 — EXTRACT COMPETITIONS
# ============================================================

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


# ============================================================
# STEP 3 — CREATE COMPETITION DATAFRAME
# ============================================================

def create_competition_dataframe(competitions):

    df = pd.DataFrame(competitions)

    return df


# ============================================================
# STEP 4 — EXTRACT CATEGORIES
# ============================================================

def extract_categories(data):

    categories = []

    for item in data["competitions"]:

        category = {
            "category_id": item["category"]["id"],
            "category_name": item["category"]["name"]
        }

        categories.append(category)

    return categories


# ============================================================
# STEP 5 — CREATE CATEGORY DATAFRAME
# ============================================================

def create_category_dataframe(categories):

    df = pd.DataFrame(categories)

    return df


# ============================================================
# STEP 6A — CHECK MISSING VALUES
# ============================================================

def check_missing_values(df, name):

    print(f"\nMissing values in {name}:")

    print(df.isnull().sum())


# ============================================================
# STEP 6B — CHECK DUPLICATE COMPETITIONS
# ============================================================

def check_duplicate_competitions(df):

    duplicates = df[
        df.duplicated(
            subset=["competition_id"],
            keep=False
        )
    ]

    print("\nDuplicate competitions:")

    if duplicates.empty:

        print("No duplicate competitions found.")

    else:

        print(duplicates)


# ============================================================
# STEP 6C — REMOVE DUPLICATE CATEGORIES
# ============================================================

def remove_duplicate_categories(df):

    df = df.drop_duplicates(
        subset=["category_id"]
    )

    return df


# ============================================================
# STEP 6D — VALIDATE CATEGORY RELATIONSHIP
# ============================================================

def validate_category_relationship(
    competitions_df,
    categories_df
):

    valid_categories = set(
        categories_df["category_id"]
    )

    invalid = competitions_df[
        ~competitions_df["category_id"].isin(
            valid_categories
        )
    ]

    print("\nInvalid category references:")

    if invalid.empty:

        print("All competition categories are valid.")

    else:

        print(invalid)


# ============================================================
# STEP 7 — SAVE PROCESSED DATA
# ============================================================

def save_processed_data(
    competitions_df,
    categories_df
):

    competitions_df.to_csv(
        COMPETITIONS_OUTPUT,
        index=False
    )

    categories_df.to_csv(
        CATEGORIES_OUTPUT,
        index=False
    )

    print("\nProcessed data saved successfully.")

    print(
        f"Saved: {COMPETITIONS_OUTPUT}"
    )

    print(
        f"Saved: {CATEGORIES_OUTPUT}"
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("COMPETITION DATA TRANSFORMATION")
    print("=" * 50)

    # Load JSON
    data = load_data()

    # Extract competitions
    competitions = extract_competitions(data)

    # Create competition DataFrame
    competitions_df = create_competition_dataframe(
        competitions
    )

    # Extract categories
    categories = extract_categories(data)

    # Create category DataFrame
    categories_df = create_category_dataframe(
        categories
    )

    # Remove duplicate categories
    categories_df = remove_duplicate_categories(
        categories_df
    )

    # Display competition data
    print("\nCompetition Data:")

    print(competitions_df)

    # Display category data
    print("\nCategory Data:")

    print(categories_df)

    # Check missing values
    check_missing_values(
        competitions_df,
        "Competitions"
    )

    check_missing_values(
        categories_df,
        "Categories"
    )

    # Check duplicate competitions
    check_duplicate_competitions(
        competitions_df
    )

    # Validate category relationship
    validate_category_relationship(
        competitions_df,
        categories_df
    )

    # Save processed data
    save_processed_data(
        competitions_df,
        categories_df
    )

    print("\n" + "=" * 50)
    print("TRANSFORMATION COMPLETED")
    print("=" * 50)