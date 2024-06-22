import pandas as pd

# Load your DataFrame from the CSV file
file_path = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Merged_Unique_Dataset.csv'
df = pd.read_csv(file_path)


# Print column names and data types
print("Column names and data types:")
for col in df.columns:
    print(f"{col}: {df[col].dtype}")

# Print total number of columns
num_columns = len(df.columns)
print(f"\nTotal number of columns: {num_columns}")


# Columns to convert to float
columns_to_convert = ['Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'Completed',
                       'Offside_pass', 'Blocked','Int Matches Played','Int Starts','Int Min',
                       'Int 90s','Int Goals','Int Assists','Int Non Penalty Goals', 
                       'Int Penalty Goals','Int Penaltes Attempted','Int Yellow Cards','Int Red Cards',
                       'Int Goals Per 90','Int Assists Per 90','Int Goals + Assits Per 90',
                       'Int Non Penalty Goals Per 90','Int Non Penalty Goals + Assits Per 90' ]


# Convert specified columns to float
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Define columns that should not be converted to numeric
non_numeric_columns = ['Player', 'League', 'Team', 'Key', 'Pos']

# Identify numeric columns by excluding non-numeric and already converted columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Generate all combinations of 'Country', 'Position', and 'Season'
all_combinations = pd.MultiIndex.from_product([
    df['Country'].unique(),
    df['Position'].unique(),
    df['Season'].unique()
], names=['Country', 'Position', 'Season']).to_frame(index=False)

# Merge with original data to ensure all combinations are included
merged_df = pd.merge(all_combinations, df, on=['Country', 'Position', 'Season'], how='left')

# Group by 'Country', 'Position', and 'Season' and aggregate numeric columns
grouped_numeric = merged_df.groupby(['Country', 'Position', 'Season']).agg({
    col: 'mean' for col in numeric_columns
}).reset_index()

# Handle non-numeric columns differently
grouped_non_numeric = merged_df.groupby(['Country', 'Position', 'Season'])[non_numeric_columns].first().reset_index()

# Merge the two grouped DataFrames
grouped_df = pd.merge(grouped_numeric, grouped_non_numeric, on=['Country', 'Position', 'Season'])

# Display the resulting DataFrame
for col in columns_to_convert:
    grouped_df[col] = pd.to_numeric(grouped_df[col], errors='coerce')

new_file_path = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Mean_Country_Data.csv'
grouped_df.to_csv(new_file_path, index=False)
print(grouped_df)
