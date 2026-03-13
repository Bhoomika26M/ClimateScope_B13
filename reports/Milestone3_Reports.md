Milestone 3 – Interactive Climate Dashboard
1. Objective
The objective of Milestone‑3 is to develop an interactive climate analytics dashboard that enables users to explore global weather data and identify climate patterns using dynamic visualizations.

The dashboard allows users to interactively filter, analyze, and visualize weather data in real time.

2. Tools Used
The following technologies were used:

Python

Streamlit – Dashboard framework

Pandas – Data processing

Plotly – Interactive visualizations

NumPy – Numerical operations

Git & GitHub – Version control

3. Dashboard Features
The ClimateScope dashboard includes several analytical components.

3.1 Global Climate Overview
Key climate indicators are displayed using KPI cards:

Average Temperature

Average Humidity

Average Wind Speed

Total Records

This provides a quick overview of global climate conditions.

3.2 Global Temperature Map
A choropleth map visualizes the average temperature distribution across different countries.

This helps identify:

Global temperature variations

Regions with extreme temperatures

3.3 Interactive Weather Map
An interactive geographical map shows weather observations using latitude and longitude coordinates.

Each marker displays:

Temperature

Humidity

Wind Speed

Users can zoom and explore weather conditions geographically.

3.4 Climate Trend Analysis
The dashboard analyzes temperature trends using time‑based aggregation.

Visualizations include:

Monthly temperature trend

Yearly climate trend

This helps identify seasonal patterns.

3.5 Regional Climate Comparison
Users can compare climate conditions between two selected countries.

Metrics compared:

Temperature

Humidity

Wind Speed

This enables regional climate analysis.

3.6 Weather Insights
Additional analytics include:

Weather condition distribution

Wind speed vs temperature analysis

These visualizations highlight relationships between climate variables.

3.7 Extreme Weather Detection
Extreme temperature events are identified using the Z‑Score anomaly detection method.

Formula used:

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

X = observed temperature

μ = mean temperature

σ = standard deviation

Records where |Z| > 3 are classified as extreme events.

4. User Interaction
The dashboard provides interactive filters including:

Country selection

Month selection

Temperature range filtering

These filters allow users to customize the analysis.

5. Output
The dashboard generates:

Interactive visualizations

Climate insights

Downloadable filtered datasets

Users can explore and export climate data directly from the dashboard.

6. Conclusion
In Milestone‑3, a fully interactive climate analytics dashboard was successfully implemented.

Key outcomes:

Global climate visualization

Climate trend analysis

Regional comparison tools

Extreme weather event detection

Interactive user interface

The dashboard transforms raw weather data into meaningful climate insights and enables users to analyze weather patterns effectively.