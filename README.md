# ClimateScope – Global Weather Analytics Dashboard

## Project Overview

ClimateScope is a data analytics project focused on analyzing global weather patterns using statistical methods and interactive visualization techniques.

The project is divided into two milestones:
- Milestone 1: Data Preparation & Initial Analysis
- Milestone 2: Statistical Analysis & Interactive Dashboard Development

---

# Milestone 1: Data Preparation & Initial Analysis

## Dataset
Source: Global Weather Repository (Kaggle)

### Dataset Overview
- Total Records: 123,941
- Total Columns: 41
- Multi-country daily weather observations
- Includes temperature, humidity, wind speed, precipitation, pressure, visibility, UV index, and air quality metrics

### Data Inspection
- Verified data types using pandas (.info())
- Generated statistical summary using (.describe())
- Checked for missing values

### Data Cleaning & Preprocessing
- Removed duplicate records
- Applied forward-fill as precautionary missing value handling
- Converted last_updated column to datetime format
- Extracted month feature
- Aggregated daily data into monthly averages grouped by country

### Output
Cleaned dataset saved at:
data/processed/cleaned_weather_data.csv

Milestone 1 successfully completed.

---

# Milestone 2: Statistical Analysis & Interactive Dashboard

## Objective
To perform statistical analysis on the cleaned dataset and develop an interactive dashboard for visualization.

## Statistical Analysis Performed
- Average temperature calculation by country
- Identification of hottest and coldest months
- Wind speed statistical analysis
- Correlation matrix between climate variables
- Extreme weather detection using boxplot analysis

## Visualization Components
- Seasonal temperature trend (Line Chart)
- Regional temperature comparison (Bar Chart)
- Correlation heatmap
- Extreme weather detection (Boxplot)
- KPI metrics (Average Temperature, Hottest Month, Coldest Month)

## Dashboard Development
The dashboard was built using Streamlit with:
- Country filter
- Month filter
- Dynamic interactive charts

## Technologies Used
- Python
- Pandas
- Plotly
- Streamlit

---

# Project Structure

ClimateScope/
├── dashboard/
├── src/
├── milestone1_report.md
├── milestone2_report.md
├── README.md
└── requirements.txt

---

# Conclusion

ClimateScope transforms raw global weather data into structured insights and interactive visualizations.

Milestone 1 focused on data preparation and cleaning.
Milestone 2 focused on statistical analysis and dashboard development.

## Milestone 3: Visualization Development & Interactivity

In this milestone, an interactive climate analytics dashboard was developed using Streamlit and Plotly.

### Features Implemented
- Interactive Streamlit dashboard
- Country and month selection filters
- Temperature range slider for dynamic analysis
- Key climate KPI metrics
- Seasonal temperature trend visualization
- Regional temperature comparison
- Correlation heatmap analysis
- Extreme weather detection
- Global temperature distribution map
- Wind speed vs temperature analysis
- Temperature distribution plots
- Key climate insights section

The dashboard enables users to explore climate patterns interactively and identify important environmental trends across different regions.