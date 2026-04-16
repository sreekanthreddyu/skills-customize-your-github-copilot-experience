# Data Cleaning Challenge - Starter Code
# Assignment: Data Cleaning Challenge
#
# Instructions:
# 1. Install dependencies: pip install pandas
# 2. Complete each section marked with TODO
# 3. Run the script with: python starter-code.py

import pandas as pd

# ── Step 1: Load and Explore the Data ─────────────────────────────────────────

# TODO: Load dirty-data.csv into a DataFrame
df = None  # replace with pd.read_csv(...)

# TODO: Print the shape (rows, columns) of the dataset

# TODO: Print the column names and their data types

# TODO: Print the number of missing values in each column

# TODO: Print the number of duplicate rows


# ── Step 2: Fix Missing Values and Duplicates ─────────────────────────────────

# TODO: Drop rows where the critical identifier column is missing (e.g., 'id' or 'name')

# TODO: Fill missing numeric columns with the mean or median of that column

# TODO: Fill missing categorical/text columns with a sensible default or most frequent value

# TODO: Remove all duplicate rows (keep the first occurrence)


# ── Step 3: Standardise and Validate ──────────────────────────────────────────

# TODO: Strip leading/trailing whitespace from all text columns

# TODO: Standardise text casing (e.g., convert 'city' column to title case)

# TODO: Convert columns to their correct data types (e.g., parse date strings, cast numeric strings)

# TODO: Identify rows with out-of-range values (e.g., negative ages) and handle them

# TODO: Save the cleaned DataFrame to clean-data.csv (index=False)
print("Cleaned data saved to clean-data.csv")
