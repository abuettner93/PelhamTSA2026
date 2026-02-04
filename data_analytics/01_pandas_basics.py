"""
01_pandas_basics.py — Loading, viewing, and exploring data
==========================================================
PREREQUISITE: Run generate_data.py first to create the CSV files!

This script teaches the absolute fundamentals of pandas:
  - Loading a CSV file into a DataFrame
  - Looking at the first/last few rows
  - Checking the shape (rows x columns)
  - Getting summary statistics
  - Selecting specific columns
  - Filtering rows based on conditions
"""

# ---- Step 1: Import pandas ---------------------------------
# "pd" is the standard nickname everyone uses for pandas.
# You'll see this in every data science project.
import pandas as pd


# ---- Step 2: Load data from a CSV file ----------------------
# pd.read_csv() reads a CSV (Comma-Separated Values) file and
# turns it into a DataFrame — think of it as a spreadsheet
# that lives inside your Python code.
housing = pd.read_csv("data/housing_data.csv")

print("=" * 60)
print("PANDAS BASICS — Housing Data")
print("=" * 60)


# ---- Step 3: Peek at the data ------------------------------
# .head() shows the first 5 rows (you can pass a number to change that)
print("\n--- First 5 rows (.head()) ---")
print(housing.head())

# .tail() shows the last 5 rows
print("\n--- Last 3 rows (.tail(3)) ---")
print(housing.tail(3))


# ---- Step 4: How big is the dataset? -----------------------
# .shape gives you (num_rows, num_columns) as a tuple
print(f"\n--- Shape ---")
print(f"Rows: {housing.shape[0]}, Columns: {housing.shape[1]}")

# .columns lists all the column names
print(f"\n--- Column names ---")
print(list(housing.columns))


# ---- Step 5: Data types and general info --------------------
# .info() prints the data type of each column, plus how many
# non-null (non-empty) values there are.  This is one of the
# FIRST things you should run on any new dataset.
print("\n--- Data types (.info()) ---")
housing.info()


# ---- Step 6: Quick statistics -------------------------------
# .describe() gives you count, mean, std, min, 25%, 50%, 75%, max
# for every numeric column.  Super useful for a quick overview!
print("\n--- Summary statistics (.describe()) ---")
print(housing.describe())


# ---- Step 7: Selecting a single column ----------------------
# Use square brackets with the column name (as a string).
# This gives you a "Series" — basically a single column.
prices = housing["price"]
print(f"\n--- Just the prices column (first 5) ---")
print(prices.head())

# You can do quick math on a Series:
print(f"\nAverage price:  ${prices.mean():,.2f}")
print(f"Highest price:  ${prices.max():,.2f}")
print(f"Lowest price:   ${prices.min():,.2f}")


# ---- Step 8: Selecting multiple columns ---------------------
# Pass a LIST of column names inside the brackets.
# Notice the double brackets: outer = indexing, inner = the list.
subset = housing[["city", "price", "bedrooms"]]
print(f"\n--- Subset of columns (first 5) ---")
print(subset.head())


# ---- Step 9: Filtering rows --------------------------------
# You can filter rows using a condition.  The condition creates
# a True/False mask, and pandas keeps only the True rows.

# Example: houses with 4 or more bedrooms
big_houses = housing[housing["bedrooms"] >= 4]
print(f"\n--- Houses with 4+ bedrooms ---")
print(f"Found {len(big_houses)} houses with 4 or more bedrooms")
print(big_houses.head())

# Example: houses in Atlanta
atlanta = housing[housing["city"] == "Atlanta"]
print(f"\n--- Houses in Atlanta ---")
print(f"Found {len(atlanta)} houses in Atlanta")
print(atlanta.head())

# Combining conditions: use & (and) or | (or)
# IMPORTANT: each condition MUST be wrapped in parentheses!
cheap_big = housing[(housing["price"] < 200000) & (housing["bedrooms"] >= 3)]
print(f"\n--- Cheap AND big (price < $200k, 3+ bedrooms) ---")
print(f"Found {len(cheap_big)} matches")
print(cheap_big.head())


# ---- Step 10: Sorting --------------------------------------
# .sort_values() sorts the DataFrame by one or more columns
most_expensive = housing.sort_values("price", ascending=False)
print(f"\n--- Top 5 most expensive houses ---")
print(most_expensive[["city", "price", "sqft", "bedrooms"]].head())


# ---- Step 11: Unique values and counts ----------------------
# .unique() returns all distinct values in a column
print(f"\n--- Unique cities ---")
print(housing["city"].unique())

# .value_counts() counts how often each value appears
print(f"\n--- How many listings per city? ---")
print(housing["city"].value_counts())


print("\n" + "=" * 60)
print("End of Lesson 1!  Try modifying the filters above and")
print("re-running the script to explore the data on your own.")
print("=" * 60)
