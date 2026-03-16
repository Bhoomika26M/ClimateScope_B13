import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/GlobalWeatherRepository.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.ffill()

# Convert date column (change column name if needed)
df['last_updated'] = pd.to_datetime(df['last_updated'])

# Create month column
df['month'] = df['last_updated'].dt.month

# Aggregate daily to monthly average
monthly_avg = df.groupby(['country', 'month']).mean(numeric_only=True).reset_index()

# Save cleaned dataset
monthly_avg.to_csv("data/processed/cleaned_weather_data.csv", index=False)

print("Milestone 1 completed successfully!")
