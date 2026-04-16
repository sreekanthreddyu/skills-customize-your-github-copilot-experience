# 📘 Assignment: Data Cleaning Challenge

## 🎯 Objective

Practice real-world data wrangling by identifying and fixing common data quality issues in a messy CSV dataset using pandas. You will handle missing values, duplicate records, inconsistent formatting, and wrong data types to produce a clean, analysis-ready dataset.

## 📝 Tasks

### 🛠️ Explore and Assess the Data

#### Description
Load the provided messy dataset and write code to identify all data quality problems before fixing anything.

#### Requirements
Completed program should:

- Load `dirty-data.csv` into a pandas DataFrame
- Display the shape, column names, and data types of the dataset
- Report the count of missing values per column
- Identify and report the number of duplicate rows

### 🛠️ Fix Missing Values and Duplicates

#### Description
Clean the dataset by handling missing values with appropriate strategies and removing duplicate rows.

#### Requirements
Completed program should:

- Drop rows where a critical column (e.g., ID or name) is missing
- Fill missing numeric values with the column mean or median
- Fill missing categorical values with a sensible default or the most frequent value
- Remove all duplicate rows from the dataset

### 🛠️ Standardise and Validate the Data

#### Description
Fix inconsistent formatting and incorrect data types so the dataset is consistent and ready for analysis.

#### Requirements
Completed program should:

- Standardise text columns (e.g., strip whitespace, fix inconsistent casing)
- Convert columns to their correct data types (e.g., dates, integers, floats)
- Identify and handle any out-of-range or clearly invalid values (e.g., negative ages)
- Save the cleaned DataFrame to a new file called `clean-data.csv`
