🌍 ClimateScope – Global Climate Analytics Dashboard
ClimateScope is a data analytics and visualization project that explores global weather data to identify climate patterns, regional differences, and extreme weather events.

The project demonstrates a complete data analytics workflow, including data preprocessing, statistical analysis, and an interactive dashboard for climate exploration.

📌 Project Objectives
The main goals of this project are:

Process and clean large weather datasets

Perform statistical climate analysis

Identify seasonal and regional climate patterns

Detect extreme weather events

Build an interactive dashboard for climate visualization

🛠 Technologies Used
The project is implemented using the following technologies:

Python

Pandas – Data manipulation

NumPy – Numerical operations

Matplotlib & Seaborn – Statistical visualization

Plotly – Interactive visualizations

Streamlit – Dashboard development

Git & GitHub – Version control

📂 Project Structure
ClimateScope
│
├── data
│   └── processed
│       └── weather_cleaned.csv
│
├── src
│   ├── preprocessing.py
│   └── analysis.py
│
├── dashboard
│   └── app.py
│
├── reports
│   ├── milestone2_report.md
│   └── milestone3_report.md
│
├── requirements.txt
└── README.md
📊 Project Milestones
Milestone 1 – Data Cleaning & Preprocessing
In this milestone, the raw weather dataset was cleaned and prepared for analysis.

Key tasks performed:

Removed duplicate records

Handled missing values

Standardized column names

Converted date fields to datetime format

Generated a cleaned dataset

Output file:

data/processed/weather_cleaned.csv
📈 Milestone 2 – Core Analysis & Visualization
Milestone‑2 focused on performing statistical analysis and generating climate insights.

Statistical Analysis
Descriptive statistics were computed for numerical variables including:

Temperature

Humidity

Wind Speed

Precipitation

Visualizations Created
Correlation Heatmap

Monthly Temperature Trends

Latitude vs Temperature Gradient

Wind Speed vs Temperature

Regional Climate Comparison

Extreme Weather Detection
Extreme weather events were identified using the Z‑Score anomaly detection method.

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

X = observed value

μ = mean

σ = standard deviation

Values where |Z| > 3 were classified as extreme events.

🌐 Milestone 3 – Interactive Climate Dashboard
Milestone‑3 introduces an interactive Streamlit dashboard that allows users to explore global climate data dynamically.

The dashboard converts raw climate data into meaningful visual insights.

📊 Dashboard Features
🌡 Climate Overview
Key climate indicators displayed as KPI metrics:

Average Temperature

Average Humidity

Average Wind Speed

Total Records

🌍 Global Temperature Map
A choropleth map visualizes the temperature distribution across countries, highlighting global climate variations.

🛰 Interactive Weather Map
A geographic map displays weather observations using latitude and longitude markers.

Each marker provides:

Temperature

Humidity

Wind Speed

📈 Climate Trend Analysis
The dashboard analyzes seasonal and long‑term climate patterns using:

Monthly Temperature Trend

Yearly Temperature Trend

🌎 Regional Climate Comparison
Users can compare climate conditions between two countries.

Metrics compared:

Average Temperature

Average Humidity

Average Wind Speed

🌦 Weather Insights
Additional visualizations include:

Weather condition distribution

Wind speed vs temperature relationship

⚠ Extreme Weather Event Detection
Extreme temperature events are detected using Z‑Score anomaly detection.

The dashboard highlights these events visually within the temperature timeline.

▶ Running the Dashboard
Install dependencies
pip install -r requirements.txt
Run the Streamlit dashboard
streamlit run dashboard/app.py
The dashboard will open automatically in your browser.

📥 Dataset
The dataset used in this project contains global weather observations including:

Temperature

Humidity

Wind Speed

Precipitation

Weather conditions

Geographic coordinates

The cleaned dataset is stored in:

data/processed/weather_cleaned.csv

👨‍💻 Author
Pranjal Sahu

ClimateScope – Climate Data Analytics Project