import streamlit as st

from queries import (
    get_competitors,
    get_competitions,
    get_venues,
    country_summary,
    complex_summary,
)

from charts import (
    points_by_player,
    competitions_by_category,
    competitions_by_gender,
    venues_by_country,
    venues_by_complex,
    movement_chart,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Tennis SportRadar Analytics",
    page_icon="🎾",
    layout="wide",
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_all_data():
    competitors = get_competitors()
    competitions = get_competitions()
    venues = get_venues()

    return competitors, competitions, venues


try:
    competitors, competitions, venues = load_all_data()

except Exception as error:
    st.error("Unable to load the database.")
    st.exception(error)
    st.stop()


# ============================================================
# HEADER
# ============================================================

st.title("🎾 Tennis SportRadar Analytics Dashboard")

st.markdown(
    """
    **Game Analytics: Unlocking Tennis Data with SportRadar API**

    Interactive analysis of competitors, rankings,
    competitions, venues and complexes.
    """
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

with st.sidebar:

    st.header("🔎 Filters")

    countries = sorted(
        competitors["country"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_countries = st.multiselect(
        "Country",
        countries,
    )

    min_points = int(
        competitors["points"].min()
        if not competitors.empty
        else 0
    )

    max_points = int(
        competitors["points"].max()
        if not competitors.empty
        else 0
    )

    selected_points = st.slider(
        "Ranking Points",
        min_value=min_points,
        max_value=max_points,
        value=(min_points, max_points),
    )

    max_rank = int(
        competitors["rank"].max()
        if not competitors.empty
        else 1
    )

    selected_rank = st.slider(
        "Maximum Rank",
        min_value=1,
        max_value=max_rank,
        value=max_rank,
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_competitors = competitors.copy()

if selected_countries:
    filtered_competitors = filtered_competitors[
        filtered_competitors["country"].isin(
            selected_countries
        )
    ]

filtered_competitors = filtered_competitors[
    (filtered_competitors["points"] >= selected_points[0])
    & (filtered_competitors["points"] <= selected_points[1])
]

filtered_competitors = filtered_competitors[
    filtered_competitors["rank"] <= selected_rank
]


# ============================================================
# KPI CARDS
# ============================================================

total_competitors = len(filtered_competitors)
total_competitions = len(competitions)
total_venues = len(venues)
total_complexes = venues["complex_name"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "👤 Competitors",
    total_competitors,
)

c2.metric(
    "🏆 Competitions",
    total_competitions,
)

c3.metric(
    "📍 Venues",
    total_venues,
)

c4.metric(
    "🏟️ Complexes",
    total_complexes,
)


st.divider()


# ============================================================
# RANKING ANALYSIS
# ============================================================

st.header("🏆 Ranking Analysis")

left, right = st.columns(2)

with left:

    st.subheader("Top Competitors by Points")

    points_data = points_by_player(
        filtered_competitors
    )

    if not points_data.empty:
        st.bar_chart(
            points_data.set_index("name")["points"]
        )
    else:
        st.info("No ranking data available.")


with right:

    st.subheader("Ranking Movement")

    movement_data = movement_chart(
        filtered_competitors
    )

    if not movement_data.empty:
        st.bar_chart(
            movement_data.set_index("name")["movement"]
        )
    else:
        st.info("No movement data available.")


st.subheader("📋 Ranking Leaderboard")

leaderboard = filtered_competitors[
    [
        "name",
        "country",
        "rank",
        "movement",
        "points",
        "competitions_played",
    ]
].sort_values("rank")

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# COUNTRY ANALYSIS
# ============================================================

st.header("🌍 Country Analysis")

country_data = country_summary(
    filtered_competitors
)

if not country_data.empty:

    left, right = st.columns(2)

    with left:

        st.subheader("Competitors by Country")

        st.bar_chart(
            country_data.set_index("country")[
                "competitors"
            ]
        )

    with right:

        st.subheader("Average Points by Country")

        st.bar_chart(
            country_data.set_index("country")[
                "average_points"
            ]
        )

    st.dataframe(
        country_data,
        use_container_width=True,
        hide_index=True,
    )


# ============================================================
# COMPETITION ANALYSIS
# ============================================================

st.header("🎾 Competition Analysis")

left, right = st.columns(2)

with left:

    st.subheader("Competitions by Category")

    category_data = competitions_by_category(
        competitions
    )

    if not category_data.empty:
        st.bar_chart(
            category_data.set_index(
                "category_name"
            )["competitions"]
        )


with right:

    st.subheader("Competitions by Gender")

    gender_data = competitions_by_gender(
        competitions
    )

    if not gender_data.empty:
        st.bar_chart(
            gender_data.set_index(
                "gender"
            )["competitions"]
        )


st.subheader("📋 Competition Details")

st.dataframe(
    competitions,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# VENUE ANALYSIS
# ============================================================

st.header("📍 Venue Analysis")

left, right = st.columns(2)

with left:

    st.subheader("Venues by Country")

    country_venue_data = venues_by_country(
        venues
    )

    if not country_venue_data.empty:
        st.bar_chart(
            country_venue_data.set_index(
                "country_name"
            )["venues"]
        )


with right:

    st.subheader("Venues by Complex")

    complex_venue_data = venues_by_complex(
        venues
    )

    if not complex_venue_data.empty:
        st.bar_chart(
            complex_venue_data.set_index(
                "complex_name"
            )["venues"]
        )


st.subheader("📋 Venue Details")

st.dataframe(
    venues,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# COMPLEX SUMMARY
# ============================================================

st.subheader("🏟️ Complex Summary")

complex_data = complex_summary(venues)

st.dataframe(
    complex_data,
    use_container_width=True,
    hide_index=True,
)


# ============================================================
# DOWNLOAD DATA
# ============================================================

st.divider()

st.header("📥 Download Data")

col1, col2, col3 = st.columns(3)

with col1:

    st.download_button(
        "Download Rankings",
        filtered_competitors.to_csv(
            index=False
        ).encode("utf-8"),
        "competitor_rankings.csv",
        "text/csv",
    )

with col2:

    st.download_button(
        "Download Competitions",
        competitions.to_csv(
            index=False
        ).encode("utf-8"),
        "competitions.csv",
        "text/csv",
    )

with col3:

    st.download_button(
        "Download Venues",
        venues.to_csv(
            index=False
        ).encode("utf-8"),
        "venues.csv",
        "text/csv",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Tennis SportRadar Analytics | "
    "API → Python → SQL → Streamlit"
)