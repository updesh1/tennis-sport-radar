# Game Analytics: Unlocking Tennis Data with SportRadar API

## Overview

Game Analytics: Unlocking Tennis Data with SportRadar API is an end-to-end sports data analytics project that collects tennis data from the SportRadar API, processes and transforms the data using Python, stores it in a relational SQL database, performs analytical queries using SQL, and presents the results through an interactive Streamlit dashboard.

The project demonstrates a complete data analytics pipeline:

SportRadar API → Python → JSON → Data Transformation → CSV → SQL Database → SQL Analysis → Streamlit Dashboard → Tennis Insights

The project focuses on tennis competition data, competition categories, tennis complexes and venues, and doubles competitor rankings.

## Project Objectives

The main objectives of this project are:

- Collect tennis data using the SportRadar API.
- Process API responses in JSON format.
- Clean and validate the collected data.
- Transform nested API data into structured relational datasets.
- Store processed data in a SQL database.
- Perform analytical queries using SQL.
- Build an interactive Streamlit dashboard.
- Provide filtering and visualization capabilities.
- Generate useful insights from tennis data.
- Demonstrate a complete real-world data analytics workflow.

## Business Use Cases

### Event Exploration

The application allows users to explore tennis competitions and understand relationships between parent competitions and sub-competitions.

### Competition Analysis

Users can analyze tennis competitions based on:

- Competition category
- Competition type
- Gender
- Competition hierarchy
- Parent and sub-competition relationships

### Venue Analysis

Users can analyze:

- Tennis venues
- Tennis complexes
- Countries
- Cities
- Venue timezones
- Number of venues per complex

### Performance Insights

Users can analyze competitor:

- Rankings
- Ranking movement
- Ranking points
- Competitions played
- Country-level statistics

### Decision Support

The project provides structured sports data that can support data-driven analysis for sports analysts, event organizers, and sports organizations.

## Data Sources

The project works with three primary data areas.

### Competition Data

Competition data contains:

- Competition ID
- Competition name
- Parent competition ID
- Competition type
- Gender
- Category ID
- Category name

### Complexes and Venues

Complex and venue data contains:

- Complex ID
- Complex name
- Venue ID
- Venue name
- City
- Country
- Country code
- Timezone
- Complex relationship

### Doubles Competitor Rankings

Competitor ranking data contains:

- Competitor ID
- Competitor name
- Country
- Country code
- Abbreviation
- Ranking
- Ranking movement
- Ranking points
- Competitions played

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | API integration, data processing and transformation |
| SportRadar API | Tennis data source |
| Pandas | Data cleaning and transformation |
| SQL | Data storage and analysis |
| SQLite | Local relational database |
| SQLAlchemy | Database connectivity |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |
| python-dotenv | Environment variable management |
| Git | Version control |
| GitHub | Team collaboration and repository hosting |

## Project Architecture

```text
                         SportRadar API
                               |
                               v
                     Python API Integration
                               |
                               v
                          JSON Data
                               |
                               v
                    Data Validation & Cleaning
                               |
                               v
                     Data Transformation
                               |
                               v
                       Processed CSV Files
                               |
                               v
                        SQL Database
                               |
                               v
                       SQL Analysis
                               |
                               v
                    Streamlit Dashboard
                               |
                               v
                       Tennis Insights
```
# Project Structure

tennis-sport-radar/
│
├── api/
│   ├── competitions.py
│   ├── competition_transform.py
│   ├── validate_competitions.py
│   ├── complexes.py
│   └── rankings.py
│
├── data/
│   ├── raw/
│   │   ├── competitions_sample.json
│   │   ├── complexes_sample.json
│   │   └── doubles_rankings_sample.json
│   │
│   └── processed/
│       ├── categories.csv
│       ├── competitions.csv
│       ├── complexes.csv
│       ├── venues.csv
│       ├── competitors.csv
│       └── competitor_rankings.csv
│
├── database/
│   ├── schema.sql
│   ├── connection.py
│   ├── insert_data.py
│   └── queries.sql
│
├── app/
│   ├── app.py
│   ├── queries.py
│   ├── charts.py
│   └── utils.py
│
├── docs/
│
├── .gitignore
├── requirements.txt
└── README.md


# Database Design
The project uses a normalized relational database consisting of six main tables.

categories
     |
     └──────── competitions


complexes
     |
     └──────── venues


competitors
     |
     └──────── competitor_rankings

# Categories Table
The categories table stores competition category information.

category_id
category_name

# Competitions Table
The competitions table stores tennis competition information.

competition_id
competition_name
parent_id
type
gender
category_id

# Venues Table
The venues table stores venue information.

venue_id
venue_name
city_name
country_name
country_code
timezone
complex_id

The complex_id column establishes a relationship between venues and complexes.

# Competitors Table
The competitors table stores competitor information.

competitor_id
name
country
country_code
abbreviation

The competitor_id column establishes a relationship between rankings and competitors.

# Installation
## 1. Clone the Repository
git clone https://github.com/updesh1/tennis-sport-radar.git

Move into the project directory:
cd tennis-sport-radar