# CS551P_Assignment_3 – World Cities Flask App 🌍

## What is this?

This README.md file shows the instructions for running the solo Flask project **World Cities App** — a global city exploration application developed as part of the solo assignment for Advanced Programming.

---

## Use of <script> in Templates

This project strictly follows the instruction that no `<script>` tags or JavaScript were used in any of the templates. All interactivity, including population bars and filtering, was achieved using Flask server logic and Jinja2 templates.

All client-side behavior is fully handled by backend rendering, without any front-end scripting or JavaScript libraries.

---

## How to run (deployed on Render)

Please visit this URL to access the deployed app:  
🔗 https://world-cities-app.onrender.com

No login is required — simply select a country and view the cities and population distribution.

---

## How to run through Codio (local version)

Use these commands:

```bash
cd flask_world_cities
python3 -m venv venv
source venv/bin/activate
pip install flask flask_sqlalchemy pandas pytest
pip freeze > requirements.txt
python3 app.py
```

Then visit this URL:  
🔗 `https://your-codio-box-url:8000`

---

## Preparations in advance if you are going to edit the assignment files

### Get Python version 3.10.7

When you open the Codio workspace, check your Python version:

```bash
python3 --version
```

If it's not 3.10.7, specify this in `runtime.txt`:

```
python-3.10.7
```

This ensures Render uses the correct Python version.

---

## Download files from GitHub repository

This project is hosted on GitHub. Clone it using:

```bash
git clone https://github.com/your-username/world-cities-app.git
```

Then:

```bash
cd world-cities-app
source venv/bin/activate
```

---

## Usage of Templates

All templates and their usage are listed below:
- `base.html` – shared layout used by all other templates (title, header, footer)

- `index.html` – dropdown to select countries
- `country.html` – shows all cities in a selected country with population bar
- `404.html` – handles "Page Not Found" errors

All templates were styled using Bootstrap and Jinja2 — no JavaScript was included.

---

## Data Sources

The dataset used in this project comes from **SimpleMaps**:  
📍 [World Cities Dataset](https://simplemaps.com/data/world-cities)

From this dataset, the `worldcities.csv` file was used as the primary source of city data.

✅ The dataset was cleaned and reduced to include only relevant fields:

- City name
- Country name
- Population
- Latitude
- Longitude

👉 The final version used in the app was limited to **5000 records** for performance and quality.

---

## Cleaning the Dataset and Reasoning Behind Reducing our Dataset

### What was done:
- Removed cities with missing names or population values
- Selected one row per city with relevant details
- Grouped cities under their parent country (for relationship integrity)

### Reasoning:
- To meet the assignment record range (2000–7000 rows)
- To simplify filtering by country
- To make loading and navigation faster
- To maintain a clean and user-friendly experience

---

## Development

- Used Flask and SQLAlchemy to build backend logic and models
- Implemented two tables: `Country` and `City` with one-to-many linkage
- Used pandas to clean and load CSV data
- Designed a dropdown country filter to display cities
- Applied Bootstrap for styling without JavaScript
- Included unit tests using `pytest`

---

## Implementation

- All routing handled in `app.py`
- Database setup using `models.py`
- Data loading + flag emoji utility in `utils.py`
- Testing written under `tests/test_routes.py`
- Custom 404 error handling
- Render deployment with `requirements.txt` and `runtime.txt`

---

## Deployment

Deployed on **Render** using:

- Python 3.10.7
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`
- Runtime file: `runtime.txt`

---

## Summary

World Cities is a solo Flask web application that allows users to browse cities by country using open geolocation data. It includes country-based filtering, a clean Bootstrap UI, and proper error handling — all without JavaScript.

The project meets all assignment requirements and is live on Render.

---

**GitHub username:** durga-0219  
**Deployment URL:** https://world-cities-app.onrender.com
