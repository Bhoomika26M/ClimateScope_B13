import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pycountry

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="ClimateScope Dashboard",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/weather_cleaned.csv")

    df["last_updated"] = pd.to_datetime(df["last_updated"])

    df["month"] = df["last_updated"].dt.month
    df["year"] = df["last_updated"].dt.year

    return df

df = load_data()

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🌍 ClimateScope – Global Climate Intelligence Dashboard")

st.markdown("""
ClimateScope analyzes **global weather data to identify climate patterns, regional differences, and extreme weather events**.

Use the filters in the sidebar to explore the climate data interactively.
""")

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("🔎 Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    sorted(df["country"].unique())
)

months = st.sidebar.multiselect(
    "Select Months",
    sorted(df["month"].unique())
)

temp_range = st.sidebar.slider(
    "Temperature Range (°C)",
    float(df["temperature_celsius"].min()),
    float(df["temperature_celsius"].max()),
    (
        float(df["temperature_celsius"].min()),
        float(df["temperature_celsius"].max())
    )
)

filtered_df = df.copy()

if countries:
    filtered_df = filtered_df[filtered_df["country"].isin(countries)]

if months:
    filtered_df = filtered_df[filtered_df["month"].isin(months)]

filtered_df = filtered_df[
    (filtered_df["temperature_celsius"] >= temp_range[0]) &
    (filtered_df["temperature_celsius"] <= temp_range[1])
]

# --------------------------------------------------
# Climate KPI Overview
# --------------------------------------------------

st.subheader("🌡 Global Climate Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average Temperature",
    f"{filtered_df['temperature_celsius'].mean():.2f} °C"
)

col2.metric(
    "Average Humidity",
    f"{filtered_df['humidity'].mean():.2f} %"
)

col3.metric(
    "Average Wind Speed",
    f"{filtered_df['wind_kph'].mean():.2f} kph"
)

col4.metric(
    "Total Records",
    filtered_df.shape[0]
)

st.markdown("---")

# --------------------------------------------------
# Dashboard Tabs
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Global Maps",
    "📈 Climate Trends",
    "🌎 Regional Analysis",
    "🌦 Weather Insights",
    "⚠ Extreme Events"
])

# --------------------------------------------------
# TAB 1 – GLOBAL MAPS
# --------------------------------------------------

with tab1:

    st.subheader("Global Temperature Distribution")

    country_avg = filtered_df.groupby("country")["temperature_celsius"].mean().reset_index()

    def get_iso3(country):
        try:
            return pycountry.countries.lookup(country).alpha_3
        except:
            return None

    country_avg["iso"] = country_avg["country"].apply(get_iso3)

    fig = px.choropleth(
        country_avg,
        locations="iso",
        color="temperature_celsius",
        hover_name="country",
        color_continuous_scale="RdYlBu_r",
        projection="natural earth",
        labels={"temperature_celsius":"Temperature (°C)"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Interactive Weather Observation Map")

    fig2 = px.scatter_geo(
        filtered_df,
        lat="latitude",
        lon="longitude",
        color="temperature_celsius",
        hover_name="country",
        hover_data={
            "temperature_celsius":True,
            "humidity":True,
            "wind_kph":True
        },
        color_continuous_scale="Turbo"
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TAB 2 – CLIMATE TRENDS
# --------------------------------------------------

with tab2:

    st.subheader("Monthly Temperature Trend")

    monthly = filtered_df.groupby("month")["temperature_celsius"].mean().reset_index()

    fig = px.line(
        monthly,
        x="month",
        y="temperature_celsius",
        markers=True,
        labels={
            "month":"Month",
            "temperature_celsius":"Temperature (°C)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Yearly Climate Trend")

    yearly = filtered_df.groupby("year")["temperature_celsius"].mean().reset_index()

    fig2 = px.line(
        yearly,
        x="year",
        y="temperature_celsius",
        markers=True,
        labels={
            "year":"Year",
            "temperature_celsius":"Average Temperature (°C)"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TAB 3 – REGIONAL ANALYSIS
# --------------------------------------------------

with tab3:

    st.subheader("Latitude vs Temperature Gradient")

    fig = px.scatter(
        filtered_df,
        x="latitude",
        y="temperature_celsius",
        color="temperature_celsius",
        opacity=0.6,
        labels={
            "latitude":"Latitude",
            "temperature_celsius":"Temperature (°C)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Country Climate Comparison")

    col1, col2 = st.columns(2)

    country1 = col1.selectbox("Select Country A", df["country"].unique())
    country2 = col2.selectbox("Select Country B", df["country"].unique())

    data1 = df[df["country"] == country1]
    data2 = df[df["country"] == country2]

    comparison = pd.DataFrame({
        "Metric": ["Temperature", "Humidity", "Wind Speed"],
        country1: [
            data1["temperature_celsius"].mean(),
            data1["humidity"].mean(),
            data1["wind_kph"].mean()
        ],
        country2: [
            data2["temperature_celsius"].mean(),
            data2["humidity"].mean(),
            data2["wind_kph"].mean()
        ]
    })

    fig2 = px.bar(
        comparison,
        x="Metric",
        y=[country1, country2],
        barmode="group",
        title="Climate Comparison"
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TAB 4 – WEATHER INSIGHTS
# --------------------------------------------------

with tab4:

    st.subheader("Weather Condition Distribution")

    if "condition_text" in filtered_df.columns:

        weather = filtered_df["condition_text"].value_counts().reset_index()

        fig = px.bar(
            weather.head(10),
            x="count",
            y="condition_text",
            orientation="h",
            labels={
                "condition_text":"Weather Condition",
                "count":"Frequency"
            }
        )

        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Wind Speed vs Temperature")

    fig2 = px.scatter(
        filtered_df,
        x="wind_kph",
        y="temperature_celsius",
        color="wind_kph",
        labels={
            "wind_kph":"Wind Speed (kph)",
            "temperature_celsius":"Temperature (°C)"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TAB 5 – EXTREME WEATHER EVENTS
# --------------------------------------------------

with tab5:

    st.subheader("Extreme Temperature Events Detection")

    mean_temp = filtered_df["temperature_celsius"].mean()
    std_temp = filtered_df["temperature_celsius"].std()

    filtered_df["z_score"] = (filtered_df["temperature_celsius"] - mean_temp) / std_temp

    extreme_df = filtered_df[np.abs(filtered_df["z_score"]) > 3]

    st.metric(
        "Extreme Temperature Events Detected",
        len(extreme_df)
    )

    fig = px.scatter(
        filtered_df,
        x="last_updated",
        y="temperature_celsius",
        labels={
            "last_updated":"Date",
            "temperature_celsius":"Temperature (°C)"
        }
    )

    fig.add_scatter(
        x=extreme_df["last_updated"],
        y=extreme_df["temperature_celsius"],
        mode="markers",
        marker=dict(color="red", size=8),
        name="Extreme Events"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Download Filtered Dataset
# --------------------------------------------------

st.subheader("📥 Download Filtered Dataset")

st.download_button(
    "Download CSV",
    filtered_df.to_csv(index=False),
    "filtered_weather_data.csv"
)

st.success("Dashboard Loaded Successfully")
