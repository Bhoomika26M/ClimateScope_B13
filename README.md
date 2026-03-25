# ClimateScope – Global Weather Analytics Dashboard

## Project Overview

ClimateScope is a data analytics project focused on analyzing global weather patterns using statistical methods and interactive visualization techniques.

The project is divided into four milestones:
- Milestone 1: Data Preparation & Initial Analysis
- Milestone 2: Statistical Analysis & Interactive Dashboard Development
- Milestone 3: Visualization Development & Interactivity
- Milestone 4: Finalization, Testing & Reporting

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

# Milestone 3: Visualization Development & Interactivity

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

---

# Milestone 4: Finalization, Testing & Reporting

## 🎯 Objective
The final milestone focuses on validating the dashboard, summarizing insights, and preparing project deliverables for presentation and evaluation.

---

## 🧪 Testing & Validation

Comprehensive testing was conducted to ensure:
- Correct data display and filtering
- Accuracy of visualizations
- Proper functioning of interactive components
- Smooth user experience across all dashboard features

### ✔️ Test Cases Covered
- Filter functionality (country, month, temperature)
- Graph updates based on user input
- Data consistency across visualizations
- Handling of empty or edge-case inputs

---

## 📊 Climate Insights & Analysis

Key regional and global insights were derived from the dataset, including:
- Identification of hottest and coldest regions
- Seasonal climate variations across countries
- Relationship between temperature, humidity, and wind speed
- Detection of extreme weather conditions

---

## 📄 Final Report

A detailed project report was prepared including:
- Methodology and data preprocessing steps
- Statistical analysis performed
- Dashboard design and features
- Key findings and interpretations

---

## 📽️ Presentation (PPT)

A structured presentation was created covering:
- Project overview and objectives
- Dataset description
- Key visualizations
- Insights and conclusions
- Demonstration of dashboard features

---

## 🌍 Final Dashboard

- Fully functional and interactive Streamlit dashboard
- User-friendly interface with dynamic filters
- Includes Smart Travel Planner for real-world application

---

# 🌍 User-Centric Enhancement

## 🔹 Smart Travel Planner (New Feature)

To extend the project beyond analysis, a **Smart Travel Planner** feature has been integrated into the dashboard.

### ✈️ Functionality
- Allows users to select:
  - Preferred temperature range
  - Month of travel
- Filters climate data to suggest suitable destinations
- Displays top matching countries with temperature and humidity details

### 💡 Impact
This feature transforms ClimateScope from a visualization tool into a **practical decision-making application**, enabling users to plan travel based on comfortable weather conditions.

---

## ▶️ How to Run the Project

1. Clone the repository  
2. Install dependencies:
   pip install -r requirements.txt
3. Place dataset file in:
   data/processed/final.parquet
4. Run the dashboard:
   streamlit run dashboard/app.py


---

## ✅ Final Outcome

ClimateScope now:
- Provides interactive climate insights  
- Supports real-world applications  
- Enables global accessibility through dashboard deployment  

This ensures the project delivers both **analytical depth and practical value**.
