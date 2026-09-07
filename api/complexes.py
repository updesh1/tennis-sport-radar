import json
import pandas as pd


# Input and output file paths
JSON_FILE = "data/raw/complexes_sample.json"

COMPLEXES_OUTPUT = "data/processed/complexes.csv"
VENUES_OUTPUT = "data/processed/venues.csv"


def load_data():
    """Load complexes and venues data from JSON file."""
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def extract_complexes(data):
    """Extract complex information from JSON."""
    complexes = []

    for item in data["complexes"]:
        complex_data = {
            "complex_id": item["id"],
            "complex_name": item["name"]
        }

        complexes.append(complex_data)

    return complexes


def extract_venues(data):
    """Extract venue information from nested complex data."""
    venues = []

    for complex_item in data["complexes"]:
        complex_id = complex_item["id"]

        for venue in complex_item["venues"]:
            venue_data = {
                "venue_id": venue["id"],
                "venue_name": venue["name"],
                "city_name": venue["city_name"],
                "country_name": venue["country_name"],
                "country_code": venue["country_code"],
                "timezone": venue["timezone"],
                "complex_id": complex_id
            }

            venues.append(venue_data)

    return venues


def create_complex_dataframe(complexes):
    """Convert complex records into a DataFrame."""
    return pd.DataFrame(complexes)


def create_venue_dataframe(venues):
    """Convert venue records into a DataFrame."""
    return pd.DataFrame(venues)


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


def validate_venue_complex_relationship(venues_df, complexes_df):
    """Check whether every venue references a valid complex."""
    valid_complex_ids = set(complexes_df["complex_id"])

    invalid_venues = venues_df[
        ~venues_df["complex_id"].isin(valid_complex_ids)
    ]

    print("\nInvalid venue-complex references:")

    if invalid_venues.empty:
        print("All venue complex references are valid.")
    else:
        print(invalid_venues)


def save_processed_data(complexes_df, venues_df):
    """Save cleaned complexes and venues data as CSV files."""
    complexes_df.to_csv(
        COMPLEXES_OUTPUT,
        index=False
    )

    venues_df.to_csv(
        VENUES_OUTPUT,
        index=False
    )

    print("\nProcessed data saved successfully.")
    print(f"Saved: {COMPLEXES_OUTPUT}")
    print(f"Saved: {VENUES_OUTPUT}")


if __name__ == "__main__":

    print("=" * 60)
    print("COMPLEX AND VENUE DATA TRANSFORMATION")
    print("=" * 60)

    # Load JSON data
    data = load_data()

    # Extract complexes and venues
    complexes = extract_complexes(data)
    venues = extract_venues(data)

    # Convert to DataFrames
    complexes_df = create_complex_dataframe(complexes)
    venues_df = create_venue_dataframe(venues)

    # Display extracted data
    print("\nComplex Data:")
    print(complexes_df)

    print("\nVenue Data:")
    print(venues_df)

    # Validate missing values
    check_missing_values(
        complexes_df,
        "Complexes"
    )

    check_missing_values(
        venues_df,
        "Venues"
    )

    # Validate duplicate IDs
    check_duplicate_ids(
        complexes_df,
        "complex_id",
        "complex IDs"
    )

    check_duplicate_ids(
        venues_df,
        "venue_id",
        "venue IDs"
    )

    # Validate relationship between venues and complexes
    validate_venue_complex_relationship(
        venues_df,
        complexes_df
    )

    # Save processed data
    save_processed_data(
        complexes_df,
        venues_df
    )

    print("\n" + "=" * 60)
    print("TRANSFORMATION COMPLETED")
    print("=" * 60)