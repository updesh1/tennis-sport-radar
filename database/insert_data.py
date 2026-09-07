import os

import pandas as pd
from sqlalchemy import text

from database.connection import get_engine


def init_schema(engine):
    """Create all database tables from schema.sql."""
    schema_path = os.path.join(
        os.path.dirname(__file__),
        "schema.sql"
    )

    with open(schema_path, "r", encoding="utf-8") as file:
        sql_statements = file.read().split(";")

    with engine.connect() as conn:
        for statement in sql_statements:
            if statement.strip():
                stmt = statement.replace(
                    "SERIAL PRIMARY KEY",
                    "INTEGER PRIMARY KEY AUTOINCREMENT"
                )
                conn.execute(text(stmt))

        conn.commit()

    print("Schema initialized successfully.")


def clear_tables(engine):
    """Clear existing data before loading fresh CSV data."""
    tables = [
        "competitor_rankings",
        "venues",
        "competitors",
        "competitions",
        "complexes",
        "categories"
    ]

    with engine.connect() as conn:
        for table in tables:
            conn.execute(text(f"DELETE FROM {table}"))

        conn.commit()

    print("Existing table data cleared.")


def insert_table_data(
    csv_file,
    table_name,
    engine,
    processed_dir
):
    """Load a CSV file into the specified database table."""
    file_path = os.path.join(
        processed_dir,
        csv_file
    )

    if not os.path.exists(file_path):
        print(f"Skipping {csv_file}: File not found.")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        print(f"Skipping {csv_file}: File is empty.")
        return

    df = df.drop_duplicates()

    try:
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        print(
            f"Loaded {len(df)} rows into '{table_name}'."
        )

    except Exception as error:
        print(
            f"Error loading {table_name}: {error}"
        )


def main():
    """Initialize database and load all processed CSV files."""
    engine = get_engine()

    # Create database tables
    init_schema(engine)

    # Remove previous data
    clear_tables(engine)

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    processed_dir = os.path.join(
        base_dir,
        "data",
        "processed"
    )

    tables = [
        ("categories.csv", "categories"),
        ("complexes.csv", "complexes"),
        ("competitors.csv", "competitors"),
        ("competitions.csv", "competitions"),
        ("venues.csv", "venues"),
        (
            "competitor_rankings.csv",
            "competitor_rankings"
        )
    ]

    for csv_file, table_name in tables:
        insert_table_data(
            csv_file,
            table_name,
            engine,
            processed_dir
        )

    print("All available data processed.")


if __name__ == "__main__":
    main()