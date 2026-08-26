import pandas as pd
from pathlib import Path

def get_matches(path: Path) -> pd.DataFrame:
    """Starter loader. Replace this with Person 3 PostgreSQL query after DB integration."""
    return pd.read_csv(path, parse_dates=["date"])

def player_summary(df: pd.DataFrame) -> pd.DataFrame:
    players = sorted(set(df["winner"]) | set(df["runner_up"]))
    rows = []
    for p in players:
        wins = int((df["winner"] == p).sum())
        matches = int(((df["winner"] == p) | (df["runner_up"] == p)).sum())
        losses = matches - wins
        win_rate = round(wins / matches * 100, 1) if matches else 0
        rows.append([p, matches, wins, losses, win_rate])
    return pd.DataFrame(rows, columns=["player","matches","wins","losses","win_rate_%"]) \
             .sort_values(["wins","win_rate_%"], ascending=False)

# PostgreSQL integration template:
#
# import os
# import psycopg2
#
# def get_matches_from_postgres():
#     conn = psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT", "5432"),
#         database=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD")
#     )
#     query = "SELECT * FROM matches;"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df
