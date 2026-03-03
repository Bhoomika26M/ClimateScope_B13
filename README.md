# ClimateScope – Global Weather Analysis

## Overview
ClimateScope is a data analytics project focused on analyzing and visualizing global weather trends using real-world weather data.

---

## Milestone 1 – Data Preparation

Tasks Completed:
- Dataset downloaded from Kaggle
- Data inspection and exploration
- Missing value handling
- Duplicate removal
- Date conversion
- Monthly aggregation
- Cleaned dataset saved

---

## Tech Stack
- Python
- Pandas
- NumPy
- Plotly
- Streamlit

---

## Project Structure

data/
  raw/
  processed/

src/
  data_processing.py

reports/
  Milestone1_Report.md

---

## Output
Cleaned dataset saved at:
data/processed/weather_cleaned.csv

---

---

# ✅ Milestone 2 – Data Analysis & Visualization

Milestone 2 focuses on extracting insights from the cleaned dataset generated in Milestone 1.

## 📊 Statistical Analysis
- Generated descriptive statistics (mean, median, std deviation, min, max)
- Saved results as:
  reports/statistical_summary.csv

## 📈 Seasonal Temperature Trend
- Converted date column to datetime
- Calculated monthly average temperature
- Visualized seasonal patterns
- Saved trend chart inside:
  reports/figures/

## 🔥 Correlation Analysis
- Generated correlation matrix
- Created heatmap visualization
- Saved inside:
  reports/figures/

## 🌡 Extreme Weather Detection
- Applied Z-score method (|Z| > 3)
- Identified extreme temperature events
- Saved results as:
  reports/extreme_weather_events.csv

## 🌍 Regional Comparison
- Identified Top 10 hottest countries
- Generated bar chart visualization

All visualizations are available in:
reports/figures/