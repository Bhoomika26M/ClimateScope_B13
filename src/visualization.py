import plotly.express as px
import plotly.graph_objects as go
from src.analysis import seasonal_trend, regional_comparison, detect_extreme_events, correlation_matrix


def line_seasonal_trend(df):
    """
    Interactive line chart for monthly temperature trend
    """
    monthly_data = seasonal_trend(df)

    fig = px.line(
        monthly_data,
        x="month",
        y="temperature_celsius",
        markers=True,
        title="Average Monthly Temperature Trend",
        labels={
            "month": "Month",
            "temperature_celsius": "Avg Temperature (°C)"
        }
    )

    return fig


def choropleth_regional_comparison(df):
    """
    Choropleth world map for average country temperature
    """
    regional_data = regional_comparison(df)

    fig = px.choropleth(
        regional_data,
        locations="country",
        locationmode="country names",
        color="temperature_celsius",
        color_continuous_scale="RdYlBu_r",
        title="Average Temperature by Country"
    )

    return fig


def extreme_events_boxplot(df):
    """
    Boxplot for temperature distribution and extreme detection
    """
    fig = px.box(
        df,
        y="temperature_celsius",
        title="Temperature Distribution & Extreme Events"
    )

    return fig


def correlation_heatmap(df):
    """
    Interactive heatmap for correlation matrix
    """
    corr = correlation_matrix(df)

    fig = go.Figure(
        data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            colorscale="RdBu",
            zmin=-1,
            zmax=1
        )
    )

    fig.update_layout(
        title="Correlation Heatmap",
        xaxis_title="Variables",
        yaxis_title="Variables"
    )

    return fig


def scatter_temp_vs_pressure(df):
    """
    Scatter plot: Temperature vs Pressure
    """
    fig = px.scatter(
        df,
        x="temperature_celsius",
        y="pressure_mb",
        color="country",
        title="Temperature vs Pressure",
        labels={
            "temperature_celsius": "Temperature (°C)",
            "pressure_mb": "Pressure (mb)"
        }
    )

    return fig