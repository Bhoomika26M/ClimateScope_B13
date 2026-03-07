import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

DATA_PATH = "data/processed/weather_cleaned.csv"
REPORT_PATH = "reports/"
FIGURE_PATH = "reports/figures/"

os.makedirs(REPORT_PATH, exist_ok=True)
os.makedirs(FIGURE_PATH, exist_ok=True)


# -------------------------------------------------
# Load Data
# -------------------------------------------------
def load_data():

    print("Loading processed dataset...")
    df = pd.read_csv(DATA_PATH)

    if "last_updated" in df.columns:
        df["last_updated"] = pd.to_datetime(df["last_updated"])

    print("Dataset Loaded:", df.shape)

    return df


# -------------------------------------------------
# Clean Statistical Summary
# -------------------------------------------------
def statistical_summary(df):

    important_cols = [
        "temperature_celsius",
        "humidity",
        "wind_kph",
        "pressure_mb",
        "precip_mm",
        "cloud",
        "uv_index"
    ]

    summary = df[important_cols].describe().round(2)

    summary.to_csv(REPORT_PATH + "clean_statistical_summary.csv")

    print("Clean statistical summary saved")


# -------------------------------------------------
# Correlation Heatmap
# -------------------------------------------------
def correlation_heatmap(df):

    cols = [
        "temperature_celsius",
        "humidity",
        "wind_kph",
        "pressure_mb",
        "precip_mm",
        "cloud",
        "uv_index",
        "visibility_km",
        "gust_kph"
    ]

    corr = df[cols].corr()

    plt.figure(figsize=(12,8))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Correlation Matrix of Key Weather Variables")

    plt.xticks(rotation=45)
    plt.yticks(rotation=0)

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "correlation_heatmap.png")
    plt.close()

    print("Correlation heatmap saved")


# -------------------------------------------------
# Seasonal Temperature Heatmap
# -------------------------------------------------
def seasonal_heatmap(df):

    df["month"] = df["last_updated"].dt.month

    seasonal = df.pivot_table(
        values="temperature_celsius",
        index="month",
        aggfunc="mean"
    )

    plt.figure(figsize=(6,6))

    sns.heatmap(
        seasonal,
        annot=True,
        cmap="YlOrRd",
        fmt=".1f"
    )

    plt.title("Seasonal Temperature Heatmap")

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "seasonal_temperature_heatmap.png")
    plt.close()

    print("Seasonal heatmap saved")


# -------------------------------------------------
# Monthly Temperature Trend
# -------------------------------------------------
def monthly_temperature_trend(df):

    df["month"] = df["last_updated"].dt.month

    monthly = df.groupby("month")["temperature_celsius"].mean()

    plt.figure(figsize=(8,5))

    monthly.plot(marker="o", color="orange")

    plt.title("Monthly Temperature Trend")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (°C)")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "monthly_temperature_trend.png")
    plt.close()

    print("Monthly temperature trend saved")


# -------------------------------------------------
# Latitude vs Temperature Gradient
# -------------------------------------------------
def latitude_temperature_gradient(df):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x=df["latitude"],
        y=df["temperature_celsius"],
        alpha=0.6
    )

    plt.title("Latitude vs Temperature Gradient")
    plt.xlabel("Latitude")
    plt.ylabel("Temperature (°C)")

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "latitude_temperature_gradient.png")
    plt.close()

    print("Latitude temperature gradient saved")


# -------------------------------------------------
# Wind Speed vs Temperature
# -------------------------------------------------
def wind_temperature_scatter(df):

    plt.figure(figsize=(8,5))

    sns.scatterplot(
        x=df["wind_kph"],
        y=df["temperature_celsius"],
        alpha=0.6
    )

    plt.title("Wind Speed vs Temperature")
    plt.xlabel("Wind Speed (kph)")
    plt.ylabel("Temperature (°C)")

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "wind_vs_temperature.png")
    plt.close()

    print("Wind vs temperature scatter saved")


# -------------------------------------------------
# Top 10 Hottest Countries
# -------------------------------------------------
def regional_temperature_comparison(df):

    top10 = (
        df.groupby("country")["temperature_celsius"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,5))

    top10.plot(kind="bar", color="tomato")

    plt.title("Top 10 Hottest Countries")
    plt.ylabel("Average Temperature (°C)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "top10_hottest_countries.png")
    plt.close()

    print("Top hottest countries chart saved")


# -------------------------------------------------
# Weather Distribution
# -------------------------------------------------
def weather_distribution(df):

    cols = [
        "temperature_celsius",
        "humidity",
        "wind_kph",
        "pressure_mb"
    ]

    df[cols].hist(
        bins=20,
        figsize=(10,8),
        color="skyblue"
    )

    plt.suptitle("Distribution of Key Weather Variables")

    plt.tight_layout()

    plt.savefig(FIGURE_PATH + "weather_distribution.png")
    plt.close()

    print("Weather distribution plots saved")


# -------------------------------------------------
# Extreme Weather Events
# -------------------------------------------------
def extreme_weather_events(df):

    events = pd.DataFrame({

        "Highest Temperature":[df["temperature_celsius"].max()],
        "Lowest Temperature":[df["temperature_celsius"].min()],
        "Highest Wind Speed":[df["wind_kph"].max()],
        "Highest Precipitation":[df["precip_mm"].max()]

    })

    events.to_csv(REPORT_PATH + "extreme_weather_events.csv", index=False)

    print("Extreme weather events saved")


# -------------------------------------------------
# Choropleth Map (NEW)
# -------------------------------------------------
def choropleth_temperature_map(df):

    country_temp = df.groupby("country")["temperature_celsius"].mean().reset_index()

    fig = px.choropleth(
        country_temp,
        locations="country",
        locationmode="ISO-3",
        color="temperature_celsius",
        color_continuous_scale="RdYlBu_r",
        title="Global Average Temperature Distribution"
    )

    fig.write_html(FIGURE_PATH + "global_temperature_choropleth.html")

    print("Global temperature choropleth map saved")


# -------------------------------------------------
# Main Execution
# -------------------------------------------------
def main():

    df = load_data()

    statistical_summary(df)

    correlation_heatmap(df)

    seasonal_heatmap(df)

    monthly_temperature_trend(df)

    latitude_temperature_gradient(df)

    wind_temperature_scatter(df)

    regional_temperature_comparison(df)

    weather_distribution(df)

    extreme_weather_events(df)

    choropleth_temperature_map(df)

    print("Milestone 2 Analysis Completed Successfully")


if __name__ == "__main__":
    main()