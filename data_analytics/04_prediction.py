"""
04_prediction.py — Predictive analytics with scikit-learn
=========================================================
PREREQUISITE: Run generate_data.py first to create the CSV files!

This script teaches the fundamentals of predictive modeling:
  - What is a "model" and why do we split data into train/test?
  - Linear Regression (the simplest predictive model)
  - Decision Tree Regressor (a step up — handles non-linear patterns)
  - How to measure if your model is any good (R², MAE, RMSE)
  - Visualizing predictions vs. actual values

GOAL: Predict a house's PRICE based on its features (sqft,
bedrooms, bathrooms, etc.)
"""

# ---- Imports ------------------------------------------------
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# scikit-learn imports — each one does a specific job:
from sklearn.model_selection import train_test_split   # splits data into train/test
from sklearn.linear_model import LinearRegression      # simple straight-line model
from sklearn.tree import DecisionTreeRegressor          # tree-based model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#                           ^^^ functions that measure how good our predictions are

sns.set_style("whitegrid")
os.makedirs("plots", exist_ok=True)


# =============================================================
# 1. LOAD AND PREPARE THE DATA
# =============================================================

housing = pd.read_csv("data/housing_data.csv")

print("=" * 60)
print("PREDICTIVE ANALYTICS — Predicting Home Prices")
print("=" * 60)

# --- Choose our features (inputs) and target (output) --------
#
# FEATURES (X): the information we GIVE the model
# TARGET   (y): the value we want the model to PREDICT
#
# Think of it like a math function:  price = f(sqft, bedrooms, ...)
# We're teaching the computer what "f" looks like by showing it
# examples from our dataset.

feature_columns = ["sqft", "bedrooms", "bathrooms", "year_built", "has_garage"]

# has_garage is True/False — we need to convert it to 1/0
# because math models only understand numbers.
housing["has_garage"] = housing["has_garage"].astype(int)

X = housing[feature_columns]   # capital X is the convention for features
y = housing["price"]           # lowercase y is the convention for the target

print("\n--- Features (X) — first 5 rows ---")
print(X.head())
print(f"\n--- Target (y) — first 5 values ---")
print(y.head())


# =============================================================
# 2. SPLIT INTO TRAINING AND TESTING SETS
# =============================================================
#
# WHY SPLIT?  If we train a model on ALL the data and then test
# it on that same data, of course it'll do well — it already
# "saw the answers."  That's like studying a test with the
# answer key and then taking the exact same test.
#
# Instead, we hide 20% of the data (the TEST set) and only let
# the model learn from the other 80% (the TRAINING set).  Then
# we check how well it predicts the 20% it never saw.

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,     # 20% for testing, 80% for training
    random_state=42,   # same seed = same split every time (reproducible)
)

print(f"\n--- Train/Test Split ---")
print(f"Training set: {len(X_train)} houses (80%)")
print(f"Testing set:  {len(X_test)} houses (20%)")


# =============================================================
# 3. MODEL #1 — LINEAR REGRESSION
# =============================================================
#
# Linear regression finds the best straight-line relationship
# between the features and the target.  It's the "hello world"
# of machine learning — simple, fast, and easy to understand.
#
# It learns something like:
#   price = (a * sqft) + (b * bedrooms) + (c * bathrooms) + ...

print("\n" + "=" * 60)
print("MODEL 1: Linear Regression")
print("=" * 60)

# Step 1: Create the model object
lr_model = LinearRegression()

# Step 2: Train (fit) it on the training data
# This is where the model "learns" the relationship.
lr_model.fit(X_train, y_train)

# Step 3: Make predictions on the TEST set
lr_predictions = lr_model.predict(X_test)

# Step 4: See what the model learned
# The "coefficients" tell you how much each feature contributes to price.
print("\n--- What the model learned ---")
print("Each coefficient = how much the price changes per 1-unit increase:\n")
for feature, coef in zip(feature_columns, lr_model.coef_):
    print(f"  {feature:15s}  {coef:>+12,.2f}")
#   Example: if sqft coefficient is +150, then each extra sqft adds ~$150
print(f"  {'(base price)':15s}  {lr_model.intercept_:>+12,.2f}")


# =============================================================
# 4. EVALUATE — How good are the predictions?
# =============================================================
#
# Three common metrics for regression (predicting a number):
#
# R² (R-squared): 0 to 1, higher is better
#   - 1.0 = perfect predictions
#   - 0.0 = model is no better than just guessing the average
#   - Think of it as "what % of the pattern did the model capture?"
#
# MAE (Mean Absolute Error): average dollar amount off
#   - "On average, predictions are off by $___"
#
# RMSE (Root Mean Squared Error): like MAE but penalizes big misses more
#   - If most predictions are close but a few are way off, RMSE will be
#     higher than MAE

def evaluate_model(name, y_actual, y_predicted):
    """Print evaluation metrics for a model's predictions."""
    r2 = r2_score(y_actual, y_predicted)
    mae = mean_absolute_error(y_actual, y_predicted)
    rmse = np.sqrt(mean_squared_error(y_actual, y_predicted))

    print(f"\n--- {name} Performance ---")
    print(f"  R² Score:  {r2:.3f}   (1.0 = perfect, 0.0 = useless)")
    print(f"  MAE:       ${mae:,.0f}   (avg $ off per prediction)")
    print(f"  RMSE:      ${rmse:,.0f}   (penalizes big misses)")
    return r2, mae, rmse


lr_r2, lr_mae, lr_rmse = evaluate_model("Linear Regression", y_test, lr_predictions)


# =============================================================
# 5. MODEL #2 — DECISION TREE
# =============================================================
#
# A decision tree makes predictions by asking a series of
# yes/no questions, like a flowchart:
#   "Is sqft > 2500?"  → Yes → "Is bedrooms > 3?" → ...
#
# It can capture non-linear patterns that linear regression misses,
# but it can also "overfit" (memorize the training data too closely).
# We limit max_depth to prevent that.

print("\n" + "=" * 60)
print("MODEL 2: Decision Tree")
print("=" * 60)

dt_model = DecisionTreeRegressor(
    max_depth=5,        # limit tree depth to prevent overfitting
    random_state=42,
)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)

dt_r2, dt_mae, dt_rmse = evaluate_model("Decision Tree", y_test, dt_predictions)

# Feature importance: the tree tells us which features it relied on most
print("\n--- Feature Importance (which features matter most?) ---")
importances = pd.Series(dt_model.feature_importances_, index=feature_columns)
importances = importances.sort_values(ascending=False)
for feature, importance in importances.items():
    bar = "#" * int(importance * 40)   # simple text-based bar chart
    print(f"  {feature:15s}  {importance:.3f}  {bar}")


# =============================================================
# 6. COMPARE THE TWO MODELS
# =============================================================

print("\n" + "=" * 60)
print("HEAD-TO-HEAD COMPARISON")
print("=" * 60)

comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Decision Tree"],
    "R²": [lr_r2, dt_r2],
    "MAE ($)": [lr_mae, dt_mae],
    "RMSE ($)": [lr_rmse, dt_rmse],
})
print("\n", comparison.to_string(index=False))

winner = "Linear Regression" if lr_r2 > dt_r2 else "Decision Tree"
print(f"\n  Better R² score: {winner}")


# =============================================================
# 7. VISUALIZE — Predicted vs. Actual prices
# =============================================================
#
# A good model's dots should cluster along the diagonal line
# (predicted = actual).  Dots far from the line are bad predictions.

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax, preds, name in [
    (axes[0], lr_predictions, "Linear Regression"),
    (axes[1], dt_predictions, "Decision Tree"),
]:
    ax.scatter(y_test, preds, alpha=0.6, color="steelblue", edgecolors="white")

    # Draw the "perfect prediction" diagonal line
    min_val = min(y_test.min(), preds.min())
    max_val = max(y_test.max(), preds.max())
    ax.plot([min_val, max_val], [min_val, max_val], "r--", linewidth=2, label="Perfect")

    ax.set_xlabel("Actual Price ($)")
    ax.set_ylabel("Predicted Price ($)")
    ax.set_title(f"{name}\nR² = {r2_score(y_test, preds):.3f}")
    ax.legend()

    # Format axes as dollars
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

plt.suptitle("Predicted vs. Actual Home Prices", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("plots/07_predicted_vs_actual.png", dpi=150)
plt.close()
print("\nSaved: plots/07_predicted_vs_actual.png")


# =============================================================
# 8. VISUALIZE — Feature importance bar chart
# =============================================================

fig, ax = plt.subplots(figsize=(8, 5))
importances.plot.barh(ax=ax, color="coral")
ax.set_xlabel("Importance (0 = not useful, 1 = most useful)")
ax.set_title("Decision Tree — Feature Importance")
ax.invert_yaxis()  # most important at the top

plt.tight_layout()
plt.savefig("plots/08_feature_importance.png", dpi=150)
plt.close()
print("Saved: plots/08_feature_importance.png")


# =============================================================
# 9. BONUS — Make a prediction on a brand-new house
# =============================================================
#
# This is the whole point of building a model: predicting values
# for data you've never seen before!

print("\n" + "=" * 60)
print("BONUS: Predict the price of a brand-new house")
print("=" * 60)

# Define a hypothetical house
new_house = pd.DataFrame([{
    "sqft": 2200,
    "bedrooms": 3,
    "bathrooms": 2,
    "year_built": 2015,
    "has_garage": 1,
}])

print("\nHouse details:")
print(f"  {new_house.iloc[0].to_dict()}")

lr_price = lr_model.predict(new_house)[0]
dt_price = dt_model.predict(new_house)[0]

print(f"\n  Linear Regression predicts: ${lr_price:,.0f}")
print(f"  Decision Tree predicts:     ${dt_price:,.0f}")


print("\n" + "=" * 60)
print("End of Lesson 4!  Experiment by changing the features,")
print("trying different max_depth values for the Decision Tree,")
print("or predicting on different hypothetical houses.")
print("=" * 60)
