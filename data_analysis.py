# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Show all columns instead of cutting middle out
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Don't wrap to new lines
pd.set_option('display.max_colwidth', None) # Show full column names

# Load the CSV file into a DataFrame
df = pd.read_csv('can_data.csv')

# Display basic information about dataset
print("Dataset Overview:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Show all column names
print("\nAll column names:")
print(df.columns.tolist())