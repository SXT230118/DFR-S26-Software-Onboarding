# Import libraries
import pandas as pd

# === Step 1: Load the CSV file into a pandas DataFrame and see what you're 
# working with

# Configure pandas display settings
pd.set_option('display.max_columns', None)  # Display all columns, no limit
# pd.set_option('display.width', None)        # Don't wrap information to next line

# Load csv file into a DataFrame
df = pd.read_csv('can_data.csv')

# Print some data here as needed instead of scrolling through csv file
print("Display overview of data: ") 
print(df.info())                            # Col names, data types, missing vals

print("First few rows: ")
print(df.head(10))

# === Cleaning data === 
# After looking
