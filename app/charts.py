import pandas as pd

def wins_by_player(df):
    out = df.groupby("winner").size().reset_index(name="wins")
    return out.sort_values("wins", ascending=False)

def wins_by_surface(df):
    out = df.groupby("surface").size().reset_index(name="wins")
    return out.sort_values("wins", ascending=False)

def competitions_by_count(df):
    out = df.groupby("competition").size().reset_index(name="matches")
    return out.sort_values("matches", ascending=False)
