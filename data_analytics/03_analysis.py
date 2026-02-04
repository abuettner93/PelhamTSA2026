"""
03_analysis.py — Deeper data analysis
======================================
PREREQUISITE: Run generate_data.py first to create the CSV files!

This script builds on the basics and teaches:
  - Grouping data and computing aggregate statistics
  - Creating new columns from existing ones
  - Correlation (how strongly two numbers are related)
  - Pivot tables (like what you'd make in Excel)
  - Presenting findings as clean formatted tables
"""

import pandas as pd

# ---- Load data ----------------------------------------------
housing = pd.read_csv("data/housing_data.csv")
vacation = pd.read_csv("data/vacation_data.csv")

print("=" * 60)
print("DATA ANALYSIS — Going Deeper")
print("=" * 60)


# =============================================================
# 1. GROUPBY — Split the data into groups and summarize
# =============================================================
# groupby() is one of the MOST powerful tools in pandas.
# Pattern:  df.groupby("column_to_group_by")["column_to_summarize"].agg_function()

print("\n--- Average price and sqft by city ---")
city_stats = housing.groupby("city").agg(
    avg_price=("price", "mean"),        # name the output column "avg_price"
    avg_sqft=("sqft", "mean"),
    num_listings=("price", "count"),     # count = number of rows in each group
).round(0)                               # round to whole numbers

# Sort by average price, highest first
city_stats = city_stats.sort_values("avg_price", ascending=False)
print(city_stats)
print()


# You can also group by MULTIPLE columns at once
print("\n--- Average price by city AND bedroom count ---")
city_bed = housing.groupby(["city", "bedrooms"])["price"].mean().round(0)
# This creates a "MultiIndex" Series — just a fancier table
print(city_bed.head(15))  # show first 15 rows to keep output manageable


# =============================================================
# 2. CREATING NEW COLUMNS
# =============================================================
# You can add new columns by doing math on existing ones.

# Price per square foot — a very common real-estate metric
housing["price_per_sqft"] = (housing["price"] / housing["sqft"]).round(2)

print("\n\n--- New column: price_per_sqft ---")
print(housing[["city", "price", "sqft", "price_per_sqft"]].head(10))

# Categorize houses by age
# We'll create a new column called "age_category"
current_year = 2026

housing["age"] = current_year - housing["year_built"]

# pd.cut() splits a continuous number into labeled buckets
housing["age_category"] = pd.cut(
    housing["age"],
    bins=[0, 10, 30, 50, 100],                           # bucket boundaries
    labels=["New (0-10)", "Mid (11-30)", "Old (31-50)", "Very Old (51+)"],
)

print("\n--- Houses by age category ---")
print(housing["age_category"].value_counts().sort_index())


# =============================================================
# 3. CORRELATION — How are two numbers related?
# =============================================================
# Correlation ranges from -1 to +1:
#   +1  = perfect positive relationship (one goes up, the other goes up)
#    0  = no relationship
#   -1  = perfect negative relationship (one goes up, the other goes down)
#
# In real life, anything above 0.5 or below -0.5 is a pretty
# strong relationship.

print("\n\n--- Correlation between numeric columns (housing) ---")
# Select only the numeric columns, then compute correlation matrix
numeric_cols = housing.select_dtypes(include="number")
correlation = numeric_cols.corr().round(2)
print(correlation)

# Let's zoom in on what correlates with price
print("\n--- What correlates with price? ---")
price_corr = correlation["price"].drop("price").sort_values(ascending=False)
print(price_corr)
print("\n(Higher positive number = stronger relationship with price)")


# =============================================================
# 4. PIVOT TABLE — Summarize data like an Excel pivot table
# =============================================================
# A pivot table lets you pick:
#   - rows    (index)
#   - columns
#   - values  (what to calculate)
#   - aggfunc (how to calculate: mean, sum, count, etc.)

print("\n\n--- Pivot Table: Average nightly rate by destination and season ---")
pivot = vacation.pivot_table(
    values="nightly_rate",
    index="destination",       # rows
    columns="season",          # columns
    aggfunc="mean",            # average
).round(2)

# Reorder columns to make seasonal sense
pivot = pivot[["winter", "spring", "summer", "fall"]]
print(pivot)


print("\n--- Pivot Table: Count of listings by destination and property type ---")
count_pivot = vacation.pivot_table(
    values="nightly_rate",
    index="destination",
    columns="property_type",
    aggfunc="count",
).fillna(0).astype(int)       # fill missing combos with 0
print(count_pivot)


# =============================================================
# 5. PUTTING IT ALL TOGETHER — A mini "report"
# =============================================================
print("\n\n" + "=" * 60)
print("MINI REPORT: Key Findings")
print("=" * 60)

# Most expensive city
top_city = city_stats["avg_price"].idxmax()  # city name with highest avg price
top_price = city_stats.loc[top_city, "avg_price"]
print(f"\n  Most expensive city:  {top_city} (avg ${top_price:,.0f})")

# Cheapest city
low_city = city_stats["avg_price"].idxmin()
low_price = city_stats.loc[low_city, "avg_price"]
print(f"  Cheapest city:        {low_city} (avg ${low_price:,.0f})")

# Most common bedroom count
top_bedrooms = housing["bedrooms"].value_counts().idxmax()
print(f"  Most common bedrooms: {top_bedrooms}")

# Best-rated vacation destination (average rating)
best_dest = vacation.groupby("destination")["rating"].mean().idxmax()
best_rating = vacation.groupby("destination")["rating"].mean().max()
print(f"  Top-rated destination: {best_dest} (avg {best_rating:.1f}/5)")

# Summer price premium for vacation rentals
summer_avg = vacation[vacation["season"] == "summer"]["nightly_rate"].mean()
other_avg = vacation[vacation["season"] != "summer"]["nightly_rate"].mean()
premium = ((summer_avg - other_avg) / other_avg) * 100
print(f"  Summer price premium: {premium:.1f}% more than other seasons")

print("\n" + "=" * 60)
print("End of Lesson 3!  Try creating your own groupby queries")
print("and pivot tables to find other interesting patterns.")
print("=" * 60)
