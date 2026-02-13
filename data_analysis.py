# Import libraries
import pandas as pd

# === Step 1: Load the CSV file into a pandas DataFrame and see what you're 
# working with
print("=== STEP 1: \n")

# Configure pandas display settings
pd.set_option('display.max_columns', None)  # Display all columns, no limit

# Load csv file into a DataFrame
df = pd.read_csv('can_data.csv')

# Print some data here as needed instead of scrolling through csv file
print("Display overview of data: ") 
print(df.info())                            # Col names, data types, missing vals

print("First few rows: ")
# print(df.head(10))
# print(df.head(20))
# print(df.head(30))
# NaN values stop between 30 and 40, maybe because car(vehicle?) was starting up
# print(df.head(40))

# === Step 2: Clean the data in some meaningful way
# When looking through the first few rows, it looks like there are a lot of NaN
# values as the vehicle gains speed. While this data could be useful, I'm removing
# it from the DataFrame so other columns could be analyzed with more complete data.
# There's a lot of data (14k+? rows in csv file), so removing ~40 rows should be
# negligible
print("\n=== STEP 2: \n")
print(f"Original rows: {len(df)}")

# Creating a new Dataframe that excludes rows missing data in certain important
# columns with engine information
df_clean = df.dropna(subset=['RPM', 'TPS', 'Coolant Temp', 'MAP', 'Air Temp', 
                             'Battery Volt'])
print(f"After removing incomplete rows: {len(df_clean)}")
print(f"Rows removed: {len(df) - len(df_clean)}")

# The current time format is in unix time, or number of seconds  since January 1,
# 1970 in UTC, so I'm changing it using the built in datetime conversion to an 
# easily readable format
df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], unit='s')

print("\nCleaned data preview:")            # Should mostly be 34 onward
print(df_clean.head())

# === Step 3: Derive some insight from the data, either a new value, or some 
# sort of statistic that can be visualized
print("\n=== STEP 3: \n")

# Basic statistics for key metrics

print("\nRPM Statistics:")
print(df_clean['RPM'].describe())

print("\nThrottle Position (TPS) Statistics:")
print(df_clean['TPS'].describe())

print("\nCoolant Temperature Statistics:")
print(df_clean['Coolant Temp'].describe())

print("\nBattery Voltage Statistics:")
print(df_clean['Battery Volt'].describe())
