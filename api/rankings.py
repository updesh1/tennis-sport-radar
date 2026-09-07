import json
import pandas as pd


# Input and output file paths
JSON_FILE = "data/raw/doubles_rankings_sample.json"

COMPETITORS_OUTPUT = "data/processed/competitors.csv"
RANKINGS_OUTPUT = "data/processed/competitor_rankings.csv"


def load_data():
    """Load doubles rankings data from JSON file."""
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def extract_competitors(data):
    """Extract competitor details from ranking data."""
    competitors = []

    for ranking_group in data["rankings"]:
        for item in ranking_group["competitor_rankings"]:

            competitor = item["competitor"]

            competitor_data = {
                "competitor_id": competitor["id"],
                "name": competitor["name"],
                "country": competitor["country"],
                "country_code": competitor["country_code"],
                "abbreviation": competitor["abbreviation"]
            }

            competitors.append(competitor_data)

    return competitors


def extract_rankings(data):
    """Extract ranking information from ranking data."""
    rankings = []

    for ranking_group in data["rankings"]:
        for item in ranking_group["competitor_rankings"]:

            ranking_data = {
                "rank": item["rank"],
                "movement": item["movement"],
                "points": item["points"],
                "competitions_played": item["competitions_played"],
                "competitor_id": item["competitor"]["id"]
            }

            rankings.append(ranking_data)

    return rankings


def create_competitor_dataframe(competitors):
    """Convert competitor records into a DataFrame."""
    return pd.DataFrame(competitors)


def create_ranking_dataframe(rankings):
    """Convert ranking records into a DataFrame."""
    return pd.DataFrame(rankings)


def check_missing_values(df, name):
    """Check for missing values."""
    print(f"\nMissing values in {name}:")
    print(df.isnull().sum())


def check_duplicate_ids(df, id_column, name):
    """Check for duplicate IDs."""
    duplicates = df[df.duplicated(subset=[id_column], keep=False)]

    print(f"\nDuplicate {name}:")

    if duplicates.empty:
        print(f"No duplicate {name} found.")
    else:
        print(duplicates)


def validate_ranking_competitor_relationship(
    rankings_df,
    competitors_df
):
    """Check that every ranking references a valid competitor."""
    valid_competitor_ids = set(
        competitors_df["competitor_id"]
    )

    invalid_rankings = rankings_df[
        ~rankings_df["competitor_id"].isin(valid_competitor_ids)
    ]

    print("\nInvalid ranking-competitor references:")

    if invalid_rankings.empty:
        print("All ranking competitor references are valid.")
    else:
        print(invalid_rankings)


def save_processed_data(
    competitors_df,
    rankings_df
):
    """Save processed competitor and ranking data as CSV files."""

    competitors_df.to_csv(
        COMPETITORS_OUTPUT,
        index=False
    )

    rankings_df.to_csv(
        RANKINGS_OUTPUT,
        index=False
    )

    print("\nProcessed data saved successfully.")
    print(f"Saved: {COMPETITORS_OUTPUT}")
    print(f"Saved: {RANKINGS_OUTPUT}")


if __name__ == "__main__":

    print("=" * 60)
    print("DOUBLES COMPETITOR RANKINGS TRANSFORMATION")
    print("=" * 60)

    # Load JSON data
    data = load_data()

    # Extract competitors and rankings
    competitors = extract_competitors(data)
    rankings = extract_rankings(data)

    # Convert to DataFrames
    competitors_df = create_competitor_dataframe(
        competitors
    )

    rankings_df = create_ranking_dataframe(
        rankings
    )

    # Display extracted data
    print("\nCompetitor Data:")
    print(competitors_df)

    print("\nRanking Data:")
    print(rankings_df)

    # Validate missing values
    check_missing_values(
        competitors_df,
        "Competitors"
    )

    check_missing_values(
        rankings_df,
        "Competitor Rankings"
    )

    # Validate duplicate competitor IDs
    check_duplicate_ids(
        competitors_df,
        "competitor_id",
        "competitor IDs"
    )

    # Validate ranking → competitor relationship
    validate_ranking_competitor_relationship(
        rankings_df,
        competitors_df
    )

    # Save processed data
    save_processed_data(
        competitors_df,
        rankings_df
    )

    print("\n" + "=" * 60)
    print("RANKINGS TRANSFORMATION COMPLETED")
    print("=" * 60)