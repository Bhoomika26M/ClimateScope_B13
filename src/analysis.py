import pandas as pd
import numpy as np


def load_data(filepath):
    df = pd.read_parquet(filepath)
    return df


def basic_statistics(df):
    """
    Return statistical summary of numeric columns
    """
    return df.describe()


def correlation_matrix(df):
    """
    Return correlation matrix of numeric columns
    """
    return df.corr(numeric_only=True)


def seasonal_trend(df, month_column="month", value_column="temperature_celsius"):
    """
    Analyze average monthly temperature trend
    """
    monthly_avg = df.groupby(month_column)[value_column].mean().reset_index()
    monthly_avg = monthly_avg.sort_values(by=month_column)
    return monthly_avg


def regional_comparison(df, region_column="country", value_column="temperature_celsius"):
    """
    Compare average temperature across countries
    """
    regional_avg = df.groupby(region_column)[value_column].mean().reset_index()
    regional_avg = regional_avg.sort_values(by=value_column, ascending=False)
    return regional_avg


def detect_extreme_events(df, column="temperature_celsius"):
    """
    Detect extreme values using IQR method
    Returns dataframe of extreme records
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    extremes = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return extremes