import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "tennis.db"


def get_connection():
    """Create a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)


def load_table(table_name):
    """Load a database table into a pandas DataFrame."""
    conn = get_connection()

    try:
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()


def get_competitors():
    """Return competitors with their ranking information."""
    conn = get_connection()

    query = """
        SELECT
            c.competitor_id,
            c.name,
            c.country,
            c.country_code,
            c.abbreviation,
            r.rank,
            r.movement,
            r.points,
            r.competitions_played
        FROM competitors c
        LEFT JOIN competitor_rankings r
            ON c.competitor_id = r.competitor_id
        ORDER BY r.rank ASC
    """

    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()


def get_competitions():
    """Return competitions with category information."""
    conn = get_connection()

    query = """
        SELECT
            comp.competition_id,
            comp.competition_name,
            comp.parent_id,
            comp.type,
            comp.gender,
            cat.category_name
        FROM competitions comp
        LEFT JOIN categories cat
            ON comp.category_id = cat.category_id
        ORDER BY comp.competition_name
    """

    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()


def get_venues():
    """Return venues with their complex information."""
    conn = get_connection()

    query = """
        SELECT
            v.venue_id,
            v.venue_name,
            v.city_name,
            v.country_name,
            v.country_code,
            v.timezone,
            c.complex_name
        FROM venues v
        LEFT JOIN complexes c
            ON v.complex_id = c.complex_id
        ORDER BY c.complex_name, v.venue_name
    """

    try:
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()


def country_summary(df):
    """Create country-level competitor statistics."""
    if df.empty:
        return pd.DataFrame()

    summary = (
        df.groupby("country", dropna=False)
        .agg(
            competitors=("competitor_id", "count"),
            average_points=("points", "mean"),
            total_points=("points", "sum"),
        )
        .reset_index()
    )

    summary["average_points"] = summary["average_points"].round(2)

    return summary.sort_values(
        "average_points",
        ascending=False,
    )


def complex_summary(df):
    """Count venues in each complex."""
    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("complex_name")
        .size()
        .reset_index(name="venues")
        .sort_values("venues", ascending=False)
    )