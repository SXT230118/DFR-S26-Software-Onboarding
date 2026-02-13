# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

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

print("\nCleaned data preview: ")            # Should mostly be 34 onward
print(df_clean.head())

# === Step 3: Derive some insight from the data, either a new value, or some 
# sort of statistic that can be visualized. I wasn't sure exactly what to do here
# because I'm not too familiar with what data is most important.
print("\n=== STEP 3: \n")

# Basic statistics for key metrics (count, mean, std, min, max, etc)
print("Basic statistics for some key metrics: ")

# RPM data
print("\nRPM Statistics:")
rpm_stats = df_clean['RPM'].describe()
print(rpm_stats)

# RPM stats analysis
print(f"The average RPM was {rpm_stats['mean']:.0f}, but the median was {rpm_stats['50%']:.0f}.")
print(f"This could mean that while the driver spent more time at lower RPMs, there were high-RPM")
print (f" moments.")

# Throttle Position Statistics
print("\nThrottle Position Statistics:")
tps_stats = df_clean['TPS'].describe()
print(tps_stats)

# Throttle Position analysis
print(f"The median throttle position was {tps_stats['50%']:.1f}%, indicating that the driver")
print(f" not really hitting the gas pedal (cruising) for most of the drive.")
print(f"However, the maximum throttle reached {tps_stats['max']:.1f}% at one point, indicating")
print(f" that the driver used full throttle at least once, maybe during a particularly long, clean")
print(f" stretch of road/track or just for occasional acceleration.")

# Coolant Temperature Statistics
print("\nCoolant Temperature Statistics:")
temp_stats = df_clean['Coolant Temp'].describe()
print(temp_stats)

# Coolant Temperature analysis
temp_range = temp_stats['max'] - temp_stats['min']
print(f"Coolant temperature didn't vary much, only {temp_range:.1f} degrees")
print(f"The low standard deviation, {temp_stats['std']:.1f}, indicates stable temperature control.")

# === Step 4: Create at least 2 different types of graphs to visualize what you came up with
print("\n=== STEP 4: \n")

# Graph 1: RPM Over Time (RPM range from analysis)
plt.figure(figsize=(12, 6))
plt.plot(df_clean['timestamp'], df_clean['RPM'], color='blue', linewidth=0.8)
plt.title('Engine RPM Over Time - Shows Range from Idle to Maximum', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('RPM', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('rpm_over_time.png', dpi=300)
print("Graph 1: rpm_over_time.png")
print("  (Visualizes the RPM range mentioned in analysis)")
plt.close()

# Graph 2: Temperature Stability Over Time
plt.figure(figsize=(12, 6))
plt.plot(df_clean['timestamp'], df_clean['Coolant Temp'], color='red', linewidth=0.8)
plt.title('Coolant Temperature Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Temperature', fontsize=12)
plt.ylim(0, 250)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_stability.png', dpi=300)
print("Graph 2: temperature_stability.png")
plt.close()

# Graph 3: RPM vs Throttle Position (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['TPS'], df_clean['RPM'], alpha=0.5, s=10, color='green')
plt.title('Engine RPM vs Throttle Position', fontsize=14, fontweight='bold')
plt.xlabel('Throttle Position (%)', fontsize=12)
plt.ylabel('RPM', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('rpm_vs_throttle.png', dpi=300)
print("Graph 3: rpm_vs_throttle.png")
plt.close()

# Graph 4: RPM Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df_clean['RPM'], bins=50, color='purple', alpha=0.7, edgecolor='black')
plt.title('Distribution of Engine RPM', fontsize=14, fontweight='bold')
plt.xlabel('RPM', fontsize=12)
plt.ylabel('Frequency (Number of Occurrences)', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('rpm_distribution.png', dpi=300)
print("Graph 4: rpm_distribution.png")
plt.close()

# Graph 5: Throttle Position Over Time
plt.figure(figsize=(12, 6))
plt.plot(df_clean['timestamp'], df_clean['TPS'], color='orange', linewidth=0.8)
plt.title('Throttle Position Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Throttle Position (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('throttle_over_time.png', dpi=300)
print("Graph 5: throttle_over_time.png")
plt.close()