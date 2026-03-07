import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pycountry
from scipy.stats import zscore
import os

# Create folders if they don't exist
os.makedirs("reports/figures", exist_ok=True)

# Load dataset
df = pd.read_csv("data/processed/weather_cleaned.csv")

# -----------------------------
# 1 Statistical Summary
# -----------------------------

numeric_df = df.select_dtypes(include="number")

stats = numeric_df.describe()
stats.to_csv("reports/statistical_summary.csv")

print("Statistical summary saved.")

# -----------------------------
# 2 Seasonal Trend Analysis
# -----------------------------

df["last_updated"] = pd.to_datetime(df["last_updated"])
df["month"] = df["last_updated"].dt.month

monthly_temp = df.groupby("month")["temperature_celsius"].mean()

plt.figure(figsize=(8,5))
monthly_temp.plot(marker="o")
plt.title("Monthly Average Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (C)")
plt.grid(True)

plt.savefig("reports/figures/monthly_temperature_trend.png")
plt.close()

print("Monthly trend saved.")

# -----------------------------
# 3 Correlation Heatmap
# -----------------------------

plt.figure(figsize=(12,8))

corr = numeric_df.corr()

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False
)

plt.title("Weather Feature Correlation Heatmap")

plt.savefig("reports/figures/correlation_heatmap.png")
plt.close()

print("Correlation heatmap saved.")

# -----------------------------
# 4 Top 10 Hottest Countries
# -----------------------------

country_temp = df.groupby("country")["temperature_celsius"].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

sns.barplot(
    x=country_temp.values,
    y=country_temp.index,
    palette="Reds_r"
)

plt.title("Top 10 Hottest Countries")
plt.xlabel("Average Temperature (C)")
plt.ylabel("Country")

plt.savefig("reports/figures/top10_hottest_countries.png")
plt.close()

print("Top countries chart saved.")

# -----------------------------
# 5 Latitude vs Temperature
# -----------------------------

if "latitude" in df.columns:

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x=df["latitude"],
        y=df["temperature_celsius"],
        alpha=0.4
    )

    plt.title("Latitude vs Temperature Gradient")
    plt.xlabel("Latitude")
    plt.ylabel("Temperature (C)")

    plt.savefig("reports/figures/latitude_temperature_gradient.png")
    plt.close()

    print("Latitude scatter saved.")

# -----------------------------
# 6 Weather Condition Distribution
# -----------------------------

if "condition_text" in df.columns:

    weather_counts = df["condition_text"].value_counts().head(10)

    plt.figure(figsize=(10,5))

    sns.barplot(
        x=weather_counts.values,
        y=weather_counts.index,
        palette="viridis"
    )

    plt.title("Weather Condition Distribution")
    plt.xlabel("Count")
    plt.ylabel("Condition")

    plt.savefig("reports/figures/weather_distribution.png")
    plt.close()

    print("Weather distribution saved.")

# -----------------------------
# 7 Extreme Weather Detection
# -----------------------------

df["zscore_temp"] = zscore(df["temperature_celsius"])

extreme = df[np.abs(df["zscore_temp"]) > 3]

extreme.to_csv("reports/extreme_weather_events.csv", index=False)

print("Extreme events saved:", len(extreme))

# -----------------------------
# 8 Choropleth Global Map
# -----------------------------

country_avg = df.groupby("country")["temperature_celsius"].mean().reset_index()

def get_iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        return None

country_avg["iso_code"] = country_avg["country"].apply(get_iso3)

fig = px.choropleth(
    country_avg,
    locations="iso_code",
    color="temperature_celsius",
    hover_name="country",
    color_continuous_scale="RdYlBu_r",
    title="Global Average Temperature Distribution"
)

fig.write_html("reports/figures/global_temperature_choropleth.html")

print("Choropleth map saved.")

print("Milestone-2 Analysis Completed Successfully.")