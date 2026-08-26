import os
import pandas as pd
from sqlalchemy import text
from database.connection import get_engine

def init_schema(engine):
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    if os.path.exists(schema_path):
        with open(schema_path, "r", encoding="utf-8") as f:
            sql_statements = f.read().split(";")
            with engine.connect() as conn:
                for statement in sql_statements:
                    if statement.strip():
                        stmt = statement.replace("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT")
                        conn.execute(text(stmt))
                conn.commit()
        print("Schema initialized successfully.")

def insert_table_data(csv_file, table_name, engine, processed_dir):
    file_path = os.path.join(processed_dir, csv_file)
    if not os.path.exists(file_path):
        print(f"Skipping {csv_file}: File not found.")
        return

    df = pd.read_csv(file_path)
    if df.empty:
        print(f"Skipping {csv_file}: File is empty.")
        return

    df = df.drop_duplicates()

    try:
        df.to_sql(table_name, engine, if_exists="append", index=False)
        print(f"Loaded {len(df)} rows into '{table_name}'.")
    except Exception as e:
        print(f"Error loading {table_name}: {e}")

def main():
    engine = get_engine()
    init_schema(engine)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(base_dir, "data", "processed")

    tables = [
        ("categories.csv", "categories"),
        ("complexes.csv", "complexes"),
        ("competitors.csv", "competitors"),
        ("competitions.csv", "competitions"),
        ("venues.csv", "venues"),
        ("competitor_rankings.csv", "competitor_rankings")
    ]

    for csv_file, table_name in tables:
        insert_table_data(csv_file, table_name, engine, processed_dir)

    print("All available data processed.")

if __name__ == "__main__":
    main()