import pandas as pd

# Load your DataFrame from the CSV file
file_path = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Merged_Unique_Dataset.csv'
df = pd.read_csv(file_path)

# Print total number of columns
num_columns = len(df.columns)
print(f"\nTotal number of columns: {num_columns}")

# Columns to avoid converting to float
columns_to_avoid = ['Player', 'League', 'Team', 'Key', 'Pos', 'Country','Season','Position']

# Identify columns to convert to float
columns_to_convert = [col for col in df.columns if col not in columns_to_avoid]

# Convert specified columns to float
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Use pivot_table to calculate the mean for each numeric column grouped by 'Country', 'Position', and 'Season'
pivot_df = df.pivot_table(
    values=columns_to_convert,  # Use all numeric columns here
    index=['Country', 'Position', 'Season'],
    aggfunc='mean'
).reset_index()

# Save the cleaned DataFrame to a CSV file
new_file_path = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Mean_Country_Data.csv'
pivot_df.to_csv(new_file_path, index=False)
print(f"Cleaned data saved to {new_file_path}")

# Print the entire NaN percentage output without skipping columns
na_percentage = pivot_df.isna().mean() * 100
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
print("\nNaN percentage per column:")
print(na_percentage)
