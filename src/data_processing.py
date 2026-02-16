import pandas as pd
import os

print("        CLIMATE SCOPE PROJECT")
print("      Milestone 1 - Data Prep")

# 1️⃣ Load Dataset

print("Loading dataset...")

file_path = "data/raw/global_weather.csv"

if not os.path.exists(file_path):
    print("Error: Dataset file not found!")
    exit()

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Original Dataset Shape:", df.shape)

# 2️⃣ Initial Data Inspection

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 3️⃣ Handle Missing Values

print("\nCleaning missing values...")

# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical (object) columns with mode
for column in df.select_dtypes(include='object'):
    df[column] = df[column].fillna(df[column].mode()[0])

print("Missing Values After Cleaning:")
print(df.isnull().sum())

# 4️⃣ Remove Duplicate Rows

print("\nRemoving duplicate rows...")
df.drop_duplicates(inplace=True)
print("New Dataset Shape:", df.shape)

# 5️⃣ Convert Date Column

print("\nConverting date column...")

if 'last_updated' in df.columns:
    df['last_updated'] = pd.to_datetime(df['last_updated'], errors='coerce')
    print("Date column converted successfully.")
else:
    print("Warning: 'last_updated' column not found.")


# 6️⃣ Monthly Aggregation

print("\nCalculating monthly average temperature...")

if 'temperature_celsius' in df.columns and 'last_updated' in df.columns:
    monthly_avg = df.groupby(
        df['last_updated'].dt.to_period('M')
    )['temperature_celsius'].mean()

    print("\nMonthly Average Temperature:")
    print(monthly_avg.head())
else:
    print("Required columns for aggregation not found.")


# 7️⃣ Save Cleaned Dataset

print("\nSaving cleaned dataset...")

output_path = "data/processed/weather_cleaned.csv"

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

df.to_csv(output_path, index=False)

print("Cleaned dataset saved at:", output_path)


print(" Milestone 1 Completed Successfully ")

