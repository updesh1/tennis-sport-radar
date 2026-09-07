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

 TechnologyPurposePythonAPI integration and data processingSportRadar APITennis data sourcePandasData cleaning and transformationSQLDatabase analysisSQLiteLocal relational databaseSQLAlchemyDatabase connectivityStreamlitInteractive dashboardPlotlyData visualizationpython-dotenvEnvironment variable managementGit / GitHubVersion control and team collaboration

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
├── .gitignore
├── requirements.txt
└── README.md

# Database Design
The project uses a normalized relational database consisting of six primary tables:

categories ───────┐
                  └────────── competitions

complexes ────────┐
                  └────────── venues

competitors ──────┐
                  └────────── competitor_rankings

- categories: category_id, category_name

- competitions: competition_id, competition_name, parent_id, type, gender, category_id

- complexes: complex_id, complex_name

- venues: venue_id, venue_name, city_name, country_name, country_code, timezone, complex_id

- competitors: competitor_id, name, country, country_code, abbreviation

- competitor_rankings: rank_id, rank, movement, points, competitions_played, competitor_id

#Installation & Setup
1. Clone the Repository
git clone [https://github.com/updesh1/tennis-sport-radar.git](https://github.com/updesh1/tennis-sport-radar.git)
cd tennis-sport-radar

2. Create a Virtual Environment
- On Windows:
python -m venv venv
- Activate in Git Bash:
source venv/Scripts/activate
- Activate in Windows Command Prompt:
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Environment Configuration
Create a .env file in the project root. The .env file is excluded via .gitignore to protect credentials.
API_KEY=your_sport_radar_api_key
DB_TYPE=sqlite
DB_NAME=tennis_db

#How to Run the Complete Project
From the project root with your virtual environment activated, run the following steps in order:

- Step 1 — Process API Data (Sample Data Workflow)
python api/competitions.py
python api/complexes.py
python api/rankings.py

- Step 2 — Load the Database

Bash
python -m database.insert_data
- Step 3 — Start the Dashboard

Bash
streamlit run app/app.py
After starting the application, open: http://localhost:8501

# Team Contributions
This project was developed collaboratively as a four-person group project using Git branches and Pull Requests.

- Person 1 (API & Competition Data): SportRadar API integration, competition/category extraction, JSON transformation, and validation.

- Person 2 (Complexes, Venues & Rankings): Complex, venue, and competitor ranking extraction, data validation, and processed CSV generation.

- Person 3 (Database & SQL): Database schema design, CSV-to-database loading, SQL analysis, and relational database implementation.

- Person 4 (Streamlit Dashboard): Database integration, UI development, filters, interactive Plotly charts, and CSV data export functionality.

# Security & Repository Notes
- Never commit sensitive data: Ensure .env, tennis.db, venv/, and __pycache__/ remain in your .gitignore.

- API Keys: Always use environment variables to load your SportRadar API key.

- Repository: https://github.com/updesh1/tennis-sport-radar
   
