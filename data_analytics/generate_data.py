"""
generate_data.py — Create sample CSV datasets for practice
===========================================================
Run this file FIRST before running any of the lesson scripts.

It creates two CSV files in a "data/" folder:
  1. housing_data.csv   — Fake home-sale listings
  2. vacation_data.csv  — Fake vacation-rental listings

WHY fake data?  Real datasets can be messy and overwhelming.
Starting with clean, predictable data lets us focus on learning
the tools before tackling real-world messiness.
"""

# ---- Imports ------------------------------------------------
import os
import random
import pandas as pd   # The main library we use to work with tables of data
import numpy as np    # Gives us tools for generating random numbers

# ---- Make results reproducible ------------------------------
# Setting a "seed" means the random numbers come out the same
# every time we run this script.  That way everyone on the team
# gets identical datasets — super helpful for comparing results!
random.seed(42)
np.random.seed(42)


def generate_housing_data(num_rows=200):
    """
    Build a fake housing dataset and return it as a pandas DataFrame.

    Columns:
      - city          : which city the house is in
      - state         : two-letter state abbreviation
      - price         : sale price in dollars
      - bedrooms      : number of bedrooms (1–6)
      - bathrooms     : number of bathrooms (1–4)
      - sqft          : square footage of the home
      - year_built    : year the house was constructed
      - has_garage    : True / False
      - listing_month : month the house was listed (1–12)
    """

    # Lists of possible values to randomly pick from
    cities_and_states = [
        ("Atlanta", "GA"),
        ("Nashville", "TN"),
        ("Charlotte", "NC"),
        ("Birmingham", "AL"),
        ("Raleigh", "NC"),
        ("Charleston", "SC"),
        ("Tampa", "FL"),
        ("Orlando", "FL"),
        ("Savannah", "GA"),
        ("Knoxville", "TN"),
    ]

    rows = []  # We'll collect each row here, then make a DataFrame at the end

    for _ in range(num_rows):
        # Pick a random city (and its matching state)
        city, state = random.choice(cities_and_states)

        bedrooms = random.randint(1, 6)
        bathrooms = random.randint(1, min(bedrooms, 4))  # bathrooms <= bedrooms, max 4
        sqft = random.randint(600, 4500)
        year_built = random.randint(1950, 2024)
        has_garage = random.choice([True, False])
        listing_month = random.randint(1, 12)

        # Price formula: loosely based on sqft and bedrooms so the numbers
        # feel realistic (but remember — this is all made-up data!)
        base_price = sqft * random.randint(100, 300)
        bedroom_bonus = bedrooms * random.randint(5000, 15000)
        price = round(base_price + bedroom_bonus, -3)  # round to nearest $1,000

        rows.append({
            "city": city,
            "state": state,
            "price": price,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sqft": sqft,
            "year_built": year_built,
            "has_garage": has_garage,
            "listing_month": listing_month,
        })

    # Create a DataFrame (basically a spreadsheet/table in Python)
    df = pd.DataFrame(rows)
    return df


def generate_vacation_data(num_rows=150):
    """
    Build a fake vacation-rental dataset and return it as a DataFrame.

    Columns:
      - destination     : vacation city
      - property_type   : "house", "condo", or "apartment"
      - nightly_rate    : price per night in dollars
      - guest_capacity  : max number of guests
      - rating          : average guest rating (1.0 – 5.0)
      - num_reviews     : how many reviews the listing has
      - has_pool        : True / False
      - season          : "winter", "spring", "summer", or "fall"
    """

    destinations = [
        "Myrtle Beach", "Destin", "Gulf Shores", "Gatlinburg",
        "Hilton Head", "Panama City Beach", "Key West",
        "Asheville", "Outer Banks", "Pigeon Forge",
    ]
    property_types = ["house", "condo", "apartment"]
    seasons = ["winter", "spring", "summer", "fall"]

    rows = []

    for _ in range(num_rows):
        destination = random.choice(destinations)
        property_type = random.choice(property_types)
        guest_capacity = random.randint(2, 12)
        has_pool = random.choice([True, False])
        season = random.choice(seasons)

        # Nightly rate depends on capacity and whether there's a pool
        base_rate = guest_capacity * random.randint(20, 60)
        pool_bonus = 50 if has_pool else 0
        # Summer costs more!
        season_multiplier = 1.4 if season == "summer" else 1.0
        nightly_rate = round((base_rate + pool_bonus) * season_multiplier, 2)

        # Rating: most places are decent (3–5 stars)
        rating = round(random.uniform(2.5, 5.0), 1)
        num_reviews = random.randint(0, 500)

        rows.append({
            "destination": destination,
            "property_type": property_type,
            "nightly_rate": nightly_rate,
            "guest_capacity": guest_capacity,
            "rating": rating,
            "num_reviews": num_reviews,
            "has_pool": has_pool,
            "season": season,
        })

    df = pd.DataFrame(rows)
    return df


# ---- Main: generate and save the CSVs ----------------------
if __name__ == "__main__":
    # Create the data/ folder if it doesn't exist yet
    os.makedirs("data", exist_ok=True)

    # Generate the housing data
    housing_df = generate_housing_data()
    housing_df.to_csv("data/housing_data.csv", index=False)
    print(f"Created data/housing_data.csv  ({len(housing_df)} rows)")

    # Generate the vacation data
    vacation_df = generate_vacation_data()
    vacation_df.to_csv("data/vacation_data.csv", index=False)
    print(f"Created data/vacation_data.csv ({len(vacation_df)} rows)")

    print("\nDone! You can now run the lesson scripts.")
