"""
02_visualization.py — Creating charts and plots
================================================
PREREQUISITE: Run generate_data.py first to create the CSV files!

This script teaches how to visualize data with matplotlib and seaborn:
  - Bar charts
  - Histograms
  - Scatter plots
  - Box plots
  - Customizing colors, labels, and titles
  - Saving plots as image files

Each plot is saved to a "plots/" folder so you can use them in
presentations or reports.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt   # The core plotting library
import seaborn as sns              # Makes matplotlib plots look nicer

# ---- Setup --------------------------------------------------
# Create a folder to save our plot images
os.makedirs("plots", exist_ok=True)

# Load both datasets
housing = pd.read_csv("data/housing_data.csv")
vacation = pd.read_csv("data/vacation_data.csv")

# Set a clean visual style for all plots
# Options include: "whitegrid", "darkgrid", "white", "dark", "ticks"
sns.set_style("whitegrid")

print("=" * 60)
print("VISUALIZATION — Creating Charts and Plots")
print("=" * 60)


# =============================================================
# PLOT 1: Bar Chart — Average home price by city
# =============================================================
# A bar chart is great for comparing a value across categories.

# Step 1: Calculate the average price for each city
avg_price_by_city = housing.groupby("city")["price"].mean().sort_values()
# groupby("city")       -> group all rows by their city
# ["price"]             -> look at just the price column
# .mean()               -> calculate the average for each group
# .sort_values()        -> sort smallest to largest

# Step 2: Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
# figsize=(width, height) in inches — controls how big the image is

# Plot horizontal bars (barh) so the city names are easy to read
ax.barh(avg_price_by_city.index, avg_price_by_city.values, color="steelblue")

# Step 3: Add labels and a title (ALWAYS label your axes!)
ax.set_xlabel("Average Price ($)")
ax.set_ylabel("City")
ax.set_title("Average Home Price by City")

# Step 4: Format the x-axis to show dollar amounts nicely
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

# Step 5: Save the plot to a file
plt.tight_layout()                        # Prevent labels from getting cut off
plt.savefig("plots/01_avg_price_by_city.png", dpi=150)
# dpi = dots per inch — higher means sharper image
plt.close()                               # Close the figure to free memory
print("Saved: plots/01_avg_price_by_city.png")


# =============================================================
# PLOT 2: Histogram — Distribution of home prices
# =============================================================
# A histogram shows how values are spread out (their "distribution").
# The x-axis is the value range, and the y-axis is how many
# data points fall in each range (called a "bin").

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(housing["price"], bins=25, color="coral", edgecolor="white")
# bins=25 means split the price range into 25 equal buckets

ax.set_xlabel("Price ($)")
ax.set_ylabel("Number of Houses")
ax.set_title("Distribution of Home Prices")
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

plt.tight_layout()
plt.savefig("plots/02_price_distribution.png", dpi=150)
plt.close()
print("Saved: plots/02_price_distribution.png")


# =============================================================
# PLOT 3: Scatter Plot — Square footage vs. price
# =============================================================
# Scatter plots help you see if two numeric variables are related.
# Each dot is one house.

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(
    housing["sqft"],       # x-axis
    housing["price"],      # y-axis
    alpha=0.5,             # transparency (0 = invisible, 1 = solid)
    color="mediumseagreen",
    edgecolors="white",
    linewidth=0.5,
)

ax.set_xlabel("Square Footage")
ax.set_ylabel("Price ($)")
ax.set_title("Home Price vs. Square Footage")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

plt.tight_layout()
plt.savefig("plots/03_price_vs_sqft.png", dpi=150)
plt.close()
print("Saved: plots/03_price_vs_sqft.png")


# =============================================================
# PLOT 4: Box Plot — Home prices by number of bedrooms
# =============================================================
# Box plots show the median, spread, and outliers of a value
# within each category.  The "box" covers the middle 50% of
# the data; the line in the middle is the median.

fig, ax = plt.subplots(figsize=(10, 6))

# seaborn makes box plots very easy
sns.boxplot(
    data=housing,
    x="bedrooms",
    y="price",
    hue="bedrooms",      # color each bedroom count differently
    palette="Blues",      # color palette
    legend=False,         # no need for a legend here
    ax=ax,                # draw on our existing axes
)

ax.set_xlabel("Number of Bedrooms")
ax.set_ylabel("Price ($)")
ax.set_title("Home Price by Bedroom Count")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

plt.tight_layout()
plt.savefig("plots/04_price_by_bedrooms.png", dpi=150)
plt.close()
print("Saved: plots/04_price_by_bedrooms.png")


# =============================================================
# PLOT 5: Bar Chart — Average vacation nightly rate by season
# =============================================================

avg_rate_by_season = vacation.groupby("season")["nightly_rate"].mean()

# Reorder seasons in a logical order (instead of alphabetical)
season_order = ["winter", "spring", "summer", "fall"]
avg_rate_by_season = avg_rate_by_season.reindex(season_order)

fig, ax = plt.subplots(figsize=(8, 5))

colors = ["#5DADE2", "#58D68D", "#F4D03F", "#EB984E"]  # custom color per season
ax.bar(avg_rate_by_season.index, avg_rate_by_season.values, color=colors)

ax.set_xlabel("Season")
ax.set_ylabel("Average Nightly Rate ($)")
ax.set_title("Vacation Rental — Average Nightly Rate by Season")

plt.tight_layout()
plt.savefig("plots/05_vacation_rate_by_season.png", dpi=150)
plt.close()
print("Saved: plots/05_vacation_rate_by_season.png")


# =============================================================
# PLOT 6: Scatter Plot — Vacation rating vs. number of reviews
# =============================================================

fig, ax = plt.subplots(figsize=(10, 6))

# Color dots by property type so we can see if there's a pattern
property_types = vacation["property_type"].unique()
colors_map = {"house": "#E74C3C", "condo": "#3498DB", "apartment": "#2ECC71"}

for ptype in property_types:
    subset = vacation[vacation["property_type"] == ptype]
    ax.scatter(
        subset["num_reviews"],
        subset["rating"],
        label=ptype,           # label for the legend
        alpha=0.6,
        color=colors_map[ptype],
    )

ax.set_xlabel("Number of Reviews")
ax.set_ylabel("Rating (out of 5)")
ax.set_title("Vacation Rental — Rating vs. Number of Reviews")
ax.legend(title="Property Type")      # Show the legend

plt.tight_layout()
plt.savefig("plots/06_rating_vs_reviews.png", dpi=150)
plt.close()
print("Saved: plots/06_rating_vs_reviews.png")


print("\n" + "=" * 60)
print("All plots saved to the plots/ folder!")
print("Open them in your file explorer or drag them into a slide deck.")
print("=" * 60)
