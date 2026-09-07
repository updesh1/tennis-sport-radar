import pandas as pd


def points_by_player(df):
    """Ranking points by competitor."""
    if df.empty:
        return pd.DataFrame(columns=["name", "points"])

    return (
        df[["name", "points"]]
        .dropna()
        .sort_values("points", ascending=False)
        .head(10)
    )


def ranking_by_player(df):
    """Top competitors by ranking."""
    if df.empty:
        return pd.DataFrame(columns=["name", "rank"])

    return (
        df[["name", "rank"]]
        .dropna()
        .sort_values("rank")
        .head(10)
    )


def competitions_by_category(df):
    """Number of competitions by category."""
    if df.empty:
        return pd.DataFrame(columns=["category_name", "competitions"])

    return (
        df.groupby("category_name")
        .size()
        .reset_index(name="competitions")
        .sort_values("competitions", ascending=False)
    )


def competitions_by_gender(df):
    """Number of competitions by gender."""
    if df.empty:
        return pd.DataFrame(columns=["gender", "competitions"])

    return (
        df.groupby("gender")
        .size()
        .reset_index(name="competitions")
    )


def venues_by_country(df):
    """Number of venues by country."""
    if df.empty:
        return pd.DataFrame(columns=["country_name", "venues"])

    return (
        df.groupby("country_name")
        .size()
        .reset_index(name="venues")
        .sort_values("venues", ascending=False)
    )


def venues_by_complex(df):
    """Number of venues by complex."""
    if df.empty:
        return pd.DataFrame(columns=["complex_name", "venues"])

    return (
        df.groupby("complex_name")
        .size()
        .reset_index(name="venues")
        .sort_values("venues", ascending=False)
    )


def movement_chart(df):
    """Show ranking movement."""
    if df.empty:
        return pd.DataFrame(columns=["name", "movement"])

    return (
        df[["name", "movement"]]
        .dropna()
        .sort_values("movement", ascending=False)
    )