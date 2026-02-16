# Milestone 1 – Data Preparation & Initial Analysis

## Project: ClimateScope – Global Weather Trends

---

## 1. Objective

The objective of Milestone 1 was to prepare the Global Weather Repository dataset for analysis and visualization by cleaning and preprocessing the data.

---

## 2. Dataset Overview

- Source: Kaggle – Global Weather Repository
- Total Records: 124,526
- Total Columns: 41
- File Format: CSV

The dataset contains weather attributes such as temperature, humidity, wind speed, precipitation, and location information.

---

## 3. Tasks Completed

### 3.1 Environment Setup
- Created project structure
- Configured virtual environment
- Installed required libraries
- Generated requirements.txt

### 3.2 Data Loading
- Downloaded dataset from Kaggle
- Stored inside `data/raw/`
- Loaded dataset using pandas

### 3.3 Data Inspection
- Checked dataset shape
- Examined column data types
- Identified missing values
- Verified duplicates

### 3.4 Data Cleaning
- Filled numeric missing values with mean
- Filled categorical missing values with mode
- Removed duplicate records

### 3.5 Data Transformation
- Converted date column to datetime format
- Performed monthly aggregation for temperature

### 3.6 Data Storage
- Saved cleaned dataset in:
data/processed/weather_cleaned.csv

---

## 4. Data Quality Issues Identified

- Missing values present in multiple columns
- Duplicate rows found and removed
- Some inconsistencies in date formatting

---

## 5. Output

- Cleaned dataset ready for visualization
- Structured project repository
- Code organized for future expansion

---

## 6. Conclusion

Milestone 1 successfully prepared the dataset for advanced analytics and dashboard development in Milestone 2.
