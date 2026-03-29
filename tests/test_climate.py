import pandas as pd

# ---------------- LOAD DATA ----------------
def load_data():
    path = "data/processed/weather_cleaned.csv"
    return pd.read_csv(path)


# ---------------- CUSTOM RISK FUNCTION ----------------
def climate_risk_score(row):
    temp = row["temperature_celsius"]
    humidity = row["humidity"]
    pm = row["air_quality_PM2.5"]

    # Simple weighted formula
    risk = (0.5 * temp) + (0.3 * humidity) + (0.2 * pm)
    return risk


# ================= TEST CASES =================

def test_data_loaded():
    df = load_data()
    assert df.shape[0] > 0


def test_columns_present():
    df = load_data()
    expected = ["country", "temperature_celsius", "humidity", "air_quality_PM2.5"]

    for col in expected:
        assert col in df.columns


def test_no_missing_values():
    df = load_data()
    assert df.isnull().sum().sum() == 0


def test_country_exists():
    df = load_data()
    countries = df["country"].unique()

    assert len(countries) > 0


def test_filtering_logic():
    df = load_data()
    country = df["country"].iloc[0]

    filtered = df[df["country"] == country]

    assert len(filtered) > 0


def test_temperature_range():
    df = load_data()
    assert df["temperature_celsius"].min() > -50
    assert df["temperature_celsius"].max() < 60


def test_risk_score_positive():
    df = load_data()

    score = climate_risk_score(df.iloc[0])

    assert score >= 0


def test_risk_score_variation():
    df = load_data()

    score1 = climate_risk_score(df.iloc[0])
    score2 = climate_risk_score(df.iloc[-1])

    assert score1 != score2 or len(df) == 1


def test_groupby_operation():
    df = load_data()

    grouped = df.groupby("country")["temperature_celsius"].mean()

    assert len(grouped) > 0


def test_empty_filter_case():
    df = load_data()

    empty = df[df["country"] == "NoCountry"]
