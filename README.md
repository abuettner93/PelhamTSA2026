# Pelham TSA 2026 — Data Science Project

A beginner-friendly data science project for learning pandas, matplotlib, and data analysis with Python.

## Quick Start

```bash
# 1. Activate the virtual environment
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate the sample datasets
python generate_data.py

# 4. Run the lessons in order
python 01_pandas_basics.py
python 02_visualization.py
python 03_analysis.py
python 04_prediction.py
```

## Project Structure

```
PelhamTSA2026/
├── requirements.txt        # Python packages to install
├── generate_data.py        # Creates sample CSV datasets
├── 01_pandas_basics.py     # Loading, filtering, sorting data
├── 02_visualization.py     # Charts and plots (saved to plots/)
├── 03_analysis.py          # Groupby, correlation, pivot tables
├── 04_prediction.py        # Predictive modeling with scikit-learn
├── data/                   # CSV files (created by generate_data.py)
│   ├── housing_data.csv
│   └── vacation_data.csv
└── plots/                  # Saved chart images (created by 02_visualization.py)
```

## Lessons Overview

| Script | What You'll Learn |
|---|---|
| `01_pandas_basics.py` | Load CSVs, view data, filter rows, sort, value counts |
| `02_visualization.py` | Bar charts, histograms, scatter plots, box plots, saving images |
| `03_analysis.py` | Groupby, new columns, correlation, pivot tables, mini report |
| `04_prediction.py` | Train/test split, Linear Regression, Decision Tree, evaluation metrics, predictions |

## Datasets

- **housing_data.csv** (200 rows) — Fake home-sale listings with price, bedrooms, sqft, city, etc.
- **vacation_data.csv** (150 rows) — Fake vacation-rental listings with nightly rate, rating, season, etc.

