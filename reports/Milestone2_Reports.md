Milestone 2 – Core Analysis & Visualization
1. Objective

The objective of Milestone-2 is to perform core analytical operations on the cleaned weather dataset and extract meaningful insights using statistical techniques and visualizations.

2. Dataset Used

The dataset used is the cleaned dataset generated from Milestone-1:

data/processed/weather_cleaned.csv

It contains:

124,000+ records

40+ weather-related features

Temperature, humidity, precipitation, wind speed, air quality indicators, etc.

3. Statistical Analysis

Numerical statistics were computed using:

df.select_dtypes(include="number").describe()

The following metrics were analyzed:

Mean

Standard deviation

Minimum

Maximum

Quartiles

📄 Output file:

reports/statistical_summary.csv
4. Seasonal Trend Analysis

The last_updated column was converted to datetime format and monthly averages were calculated.

df["month"] = pd.to_datetime(df["last_updated"]).dt.month
df.groupby("month")["temperature_celsius"].mean()

📈 Visualization:

Monthly Average Temperature Trend (Line Chart)

📁 Saved as:

reports/figures/monthly_temperature_trend.png
5. Correlation Analysis

Correlation matrix was computed on numeric features:

numeric_df.corr()

🔥 Visualization:

Correlation Heatmap

📁 Saved as:

reports/figures/correlation_heatmap.png
Insight:

Moderate relationship observed between temperature and humidity.

Wind speed shows weak correlation with temperature.

6. Regional Comparison

Average temperature was calculated country-wise:

df.groupby("country")["temperature_celsius"].mean()

📊 Visualization:

Top 10 Hottest Countries (Bar Chart)

📁 Saved as:

reports/figures/top10_hottest_countries.png
7. Extreme Weather Event Detection

Z-Score method was used to detect anomalies.

Formula used:

Z = (X − μ) / σ

Records where |Z| > 3 were classified as extreme events.

📄 Output:

reports/extreme_weather_events.csv

Detected Extreme Events: 884

8. Tools Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Git (Version Control)

9. Conclusion

In Milestone-2:

Statistical analysis was successfully performed.

Seasonal trends were identified.

Correlation between weather variables was analyzed.

Extreme weather events were detected using Z-Score.

Multiple visualizations were generated.

This milestone establishes a strong analytical foundation for building an interactive dashboard in Milestone-3.