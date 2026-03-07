Milestone 2 – Core Analysis & Visualization
1. Objective
The objective of Milestone‑2 is to perform core analytical operations on the cleaned weather dataset and extract meaningful insights using statistical techniques and visualizations.
This stage focuses on identifying patterns, correlations, seasonal variations, and extreme weather conditions using data analysis and visualization techniques.

2. Dataset Used
The dataset used in this milestone is the cleaned dataset generated from Milestone‑1.

Dataset Location

data/processed/weather_cleaned.csv
Dataset Characteristics
124,000+ records

40+ weather‑related attributes

Includes various meteorological parameters such as:

• Temperature
• Humidity
• Wind Speed
• Precipitation
• Air Quality Indicators
• Atmospheric Conditions
• Geographic Information (Country, Latitude, Longitude)

This dataset serves as the foundation for performing statistical analysis and extracting climate insights.

3. Statistical Analysis
Basic statistical metrics were computed for all numeric variables in the dataset using Pandas descriptive statistics.

Code Used
df.select_dtypes(include="number").describe()
Metrics Analyzed
The following statistical measures were calculated:

Mean

Standard Deviation

Minimum Value

Maximum Value

Quartiles (25%, 50%, 75%)

Output File
reports/statistical_summary.csv
This file provides a summarized view of all numerical weather attributes.

4. Seasonal Trend Analysis
To analyze seasonal temperature trends, the last_updated column was converted to a datetime format and monthly averages were calculated.

Code Used
df["month"] = pd.to_datetime(df["last_updated"]).dt.month
df.groupby("month")["temperature_celsius"].mean()
Visualization Generated
📈 Monthly Average Temperature Trend (Line Chart)

This chart shows how average temperature varies across different months of the year.

Output File
reports/figures/monthly_temperature_trend.png
Insight
Temperature patterns follow seasonal cycles.

Some months show noticeably higher average temperatures indicating warmer seasons.

5. Correlation Analysis
To understand relationships between weather variables, a correlation matrix was computed for all numeric features.

Code Used
numeric_df.corr()
Visualization Generated
🔥 Correlation Heatmap

The heatmap visually represents relationships between different weather attributes.

Output File
reports/figures/correlation_heatmap.png
Key Observations
Moderate correlation observed between temperature and humidity.

Wind speed shows weak correlation with temperature.

Some atmospheric indicators show interdependency.

6. Regional Temperature Comparison
To identify regions experiencing higher temperatures, the average temperature was computed country‑wise.

Code Used
df.groupby("country")["temperature_celsius"].mean()
Visualization Generated
📊 Top 10 Hottest Countries (Bar Chart)

This chart highlights countries with the highest average temperatures.

Output File
reports/figures/top10_hottest_countries.png
7. Latitude vs Temperature Analysis
Temperature patterns were also analyzed based on geographical latitude to understand global climate gradients.

Visualization Generated
📍 Latitude vs Temperature Gradient (Scatter Plot)

Output File
reports/figures/latitude_temperature_gradient.png
Insight
Temperatures tend to decrease as distance from the equator increases.

Equatorial regions show consistently higher temperatures.

8. Weather Condition Distribution
To understand the frequency of different weather conditions, the distribution of weather types was analyzed.

Visualization Generated
📊 Weather Condition Distribution (Bar Chart)

Output File
reports/figures/weather_distribution.png
This chart shows how frequently different weather conditions occur within the dataset.

9. Extreme Weather Event Detection
Extreme weather events were detected using the Z‑Score statistical method.

Formula Used
Z
=
X
−
μ
σ
Z= 
σ
X−μ
​
 
Where:

X = Data point

μ = Mean

σ = Standard Deviation

Records with:

|Z| > 3
were classified as extreme weather events.

Output File
reports/extreme_weather_events.csv
Results
Detected Extreme Weather Events: 884

These records represent unusual weather conditions that deviate significantly from the dataset's average patterns.

10. Global Temperature Visualization
A choropleth world map was created to visualize the distribution of temperature across different countries.

Visualization Generated
🌍 Global Temperature Choropleth Map

Output File
reports/figures/global_temperature_choropleth.html
This interactive map provides a geographical representation of temperature variations around the world.

11. Tools & Technologies Used
The following tools and libraries were used in this milestone:

Python

Pandas – Data manipulation

NumPy – Numerical computations

Matplotlib – Data visualization

Seaborn – Statistical visualizations

Plotly – Interactive geographical visualization

Git & GitHub – Version control and collaboration

12. Conclusion
In Milestone‑2, the cleaned weather dataset was successfully analyzed using statistical and visualization techniques.

The following tasks were accomplished:

✔ Statistical summary of weather variables
✔ Seasonal temperature trend analysis
✔ Correlation analysis between weather parameters
✔ Regional temperature comparison
✔ Latitude‑based climate analysis
✔ Weather condition distribution analysis
✔ Extreme weather event detection using Z‑Score
✔ Global temperature visualization using a choropleth map

These analyses provide valuable insights into global climate patterns and lay the groundwork for building an interactive climate monitoring dashboard in Milestone‑3.

