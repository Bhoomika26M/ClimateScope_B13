# CLIMATE SCOPE PROJECT
# Milestone 2 – Core Analysis & Visualization

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Paths

DATA_PATH = "data/processed/weather_cleaned.csv"
REPORT_PATH = "reports"
FIGURE_PATH = os.path.join(REPORT_PATH, "figures")

os.makedirs(REPORT_PATH, exist_ok=True)
os.makedirs(FIGURE_PATH, exist_ok=True)

print("CLIMATE SCOPE PROJECT")
print("Milestone 2 – Core Analysis & Visualization\n")

# Load dataset

print("Loading cleaned dataset...")
df = pd.read_csv(DATA_PATH)
print("Dataset loaded successfully!")
print(f"Dataset Shape: {df.shape}\n")

print("Columns:", list(df.columns), "\n")

# Select numeric columns safely

numeric_df = df.select_dtypes(include="number")

# Statistical Analysis

print("Performing statistical analysis...")
stats = numeric_df.describe()
stats.to_csv(os.path.join(REPORT_PATH, "statistical_summary.csv"))
print("Statistical summary saved.\n")

# Seasonal / Monthly Trend Analysis

if "last_updated" in df.columns:
    df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")
    df["month"] = df["last_updated"].dt.month

    if "temperature_celsius" in df.columns:
        monthly_temp = (
            df.groupby("month")["temperature_celsius"]
            .mean()
            .reset_index()
        )

        plt.figure(figsize=(8, 5))
        plt.plot(monthly_temp["month"], monthly_temp["temperature_celsius"], marker="o")
        plt.title("Monthly Average Temperature Trend")
        plt.xlabel("Month")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(FIGURE_PATH, "monthly_temperature_trend.png"))
        plt.close()

        print("Seasonal temperature trend analyzed.\n")

# Correlation Analysis

print("Performing correlation analysis...")

corr_data = numeric_df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_data, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_PATH, "correlation_heatmap.png"))
plt.close()

print("Correlation heatmap saved.\n")

# Top 10 Hottest Countries

if "country" in df.columns and "temperature_celsius" in df.columns:
    country_avg = (
        df.groupby("country")["temperature_celsius"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(9, 5))
    country_avg.plot(kind="bar")
    plt.title("Top 10 Hottest Countries (Average Temperature)")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURE_PATH, "top10_hottest_countries.png"))
    plt.close()

    print("Top 10 hottest countries chart saved.\n")

# Extreme Weather Event Detection (Z-Score)

if "temperature_celsius" in df.columns:
    temp_mean = df["temperature_celsius"].mean()
    temp_std = df["temperature_celsius"].std()

    df["z_score_temp"] = (df["temperature_celsius"] - temp_mean) / temp_std

    extreme_events = df[np.abs(df["z_score_temp"]) > 3]

    extreme_events.to_csv(
        os.path.join(REPORT_PATH, "extreme_weather_events.csv"),
        index=False
    )

    print("Extreme events detected:", len(extreme_events), "\n")

# Project Completion

print("Milestone 2 Analysis Completed Successfully!")