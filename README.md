# Tennis SportRadar Analytics — Person 4

## Person 4 responsibility
Streamlit dashboard, visualizations, filters and final integration.

## Run locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/app.py
```

## Dataset
`data/processed/tennis_matches.csv` is a synthetic starter dataset for dashboard development/testing.
Replace it with the cleaned project data from Persons 1–3 when available.

## Git branch
`person-4-dashboard`

## Git workflow
```bash
git checkout main
git pull origin main
git checkout person-4-dashboard
git add .
git commit -m "Add Streamlit tennis dashboard"
git push origin person-4-dashboard
```
