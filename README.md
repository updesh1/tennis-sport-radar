# Game Analytics: Unlocking Tennis Data with SportRadar API

## Project Overview

**Game Analytics: Unlocking Tennis Data with SportRadar API** is an end-to-end sports data analytics project developed to collect, transform, store, analyze, and visualize tennis data. 

The project uses the SportRadar API as the primary data source. The API returns tennis information in JSON format, which is processed using Python and transformed into structured relational data. The processed data is stored in a SQL database and analyzed using SQL queries. Finally, an interactive Streamlit dashboard presents the results through tables, filters, KPIs, and visualizations.

**The Complete Pipeline:**
```text
SportRadar API
      ↓
Python API Integration
      ↓
JSON Data
      ↓
Data Cleaning & Transformation
      ↓
Processed CSV Files
      ↓
SQL Database
      ↓
SQL Queries & Analysis
      ↓
Streamlit Dashboard
      ↓
Tennis Insights
```
This project is designed for sports enthusiasts, analysts, event organizers, and organizations that want to explore tennis competition structures, venues, rankings, and related insights.

# Objectives
- Collect tennis data using the SportRadar API.

- Process and validate API JSON responses.

- Transform nested API data into structured datasets.

- Store the processed data in a relational SQL database.

- Analyze tennis data using SQL queries.

- Build an interactive Streamlit dashboard.

- Provide filters and visualizations for exploring tennis data.

- Demonstrate a complete real-world data analytics workflow.

# Business Use Cases
- Event Exploration: Understand competition relationships, including parent and sub-competitions.

- Competition Analysis: Analyze competitions based on category, gender, type, and hierarchy.

- Venue Analysis: Explore tennis venues, countries, cities, complexes, timezones, and the number of venues per complex.

- Performance Insights: Analyze competitor rankings, movement, points, competitions played, and country-level performance.

- Decision Support: Help analysts and sports organizations understand competition structures, venue distribution, and competitor performance.

# Data Sources
## Competition Data
Maintains the relationship between competitions and categories.

- Fields: Competition ID, Name, Parent competition, Type, Gender, Category

##Complexes and Venues
- Complexes: Complex ID, Complex name

- Venues: Venue ID, Venue name, City, Country, Country code, Timezone, Complex relationship

## Doubles Competitor Rankings
- Fields: Competitor ID, Name, Country, Country code, Abbreviation, Ranking, Ranking movement, Ranking points, Competitions played

#Technology Stack
Technology,Purpose
Python,API integration and data processing
SportRadar API,Tennis data source
Pandas,Data cleaning and transformation
SQL,Database analysis
SQLite,Local relational database
SQLAlchemy,Database connectivity
Streamlit,Interactive dashboard
Plotly,Data visualization
python-dotenv,Environment variable management
Git / GitHub,Version control and team collaboration
