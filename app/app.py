import streamlit as st
import pandas as pd
from pathlib import Path
from queries import get_matches, player_summary
from charts import wins_by_player, wins_by_surface, competitions_by_count

st.set_page_config(page_title="Tennis SportRadar Analytics", page_icon="🎾", layout="wide")

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "processed" / "tennis_matches.csv"

st.title("🎾 Tennis SportRadar Analytics Dashboard")
st.caption("Person 4 — Streamlit Dashboard / Final Integration")

@st.cache_data
def load_data():
    return get_matches(DATA_PATH)

df = load_data()

with st.sidebar:
    st.header("Filters")
    players = sorted(set(df["winner"]) | set(df["runner_up"]))
    player = st.multiselect("Player", players)
    surfaces = sorted(df["surface"].dropna().unique())
    surface = st.multiselect("Surface", surfaces)
    countries = sorted(df["country"].dropna().unique())
    country = st.multiselect("Country", countries)

filtered = df.copy()
if player:
    filtered = filtered[
        filtered["winner"].isin(player) | filtered["runner_up"].isin(player)
    ]
if surface:
    filtered = filtered[filtered["surface"].isin(surface)]
if country:
    filtered = filtered[filtered["country"].isin(country)]

total_matches = len(filtered)
total_players = len(set(filtered["winner"]) | set(filtered["runner_up"]))
total_competitions = filtered["competition"].nunique()
total_countries = filtered["country"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Matches", total_matches)
c2.metric("Players", total_players)
c3.metric("Competitions", total_competitions)
c4.metric("Countries", total_countries)

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("🏆 Wins by Player")
    st.bar_chart(wins_by_player(filtered), x="player", y="wins")
with right:
    st.subheader("🎾 Wins by Surface")
    st.bar_chart(wins_by_surface(filtered), x="surface", y="wins")

st.subheader("📊 Competitions")
st.bar_chart(competitions_by_count(filtered), x="competition", y="matches")

st.subheader("📋 Match Data")
st.dataframe(filtered.sort_values("date", ascending=False), use_container_width=True)

st.subheader("👤 Player Summary")
summary = player_summary(filtered)
st.dataframe(summary, use_container_width=True)

st.download_button(
    "Download filtered data",
    filtered.to_csv(index=False).encode("utf-8"),
    "filtered_tennis_matches.csv",
    "text/csv"
)
