import pandas as pd
import numpy as np

# Load the mean data file into a DataFrame
mean_data_file = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Mean_Country_Data.csv'
df = pd.read_csv(mean_data_file)

# Define grouping columns and numeric columns
group_columns = ['Season', 'Country']
numeric_columns = df.select_dtypes(include='number').columns

# Function to fill NaN values with largest value for 'Country' and 'Season'
def fill_with_largest_or_lowest_or_average_of_3(row):
    if row[numeric_columns].isna().any():
        season = row['Season']
        country = row['Country']
        position = row.get('Position', np.nan)
        
        # Check if there are rows with data for the same 'Season' and 'Country'
        country_season_data = df[(df['Season'] == season) & (df['Country'] == country) & (~df[numeric_columns].isna().all(axis=1))]
        
        if len(country_season_data) > 0:
            # Use the largest value for each numeric column
            for col in numeric_columns:
                if pd.isna(row[col]):
                    row[col] = country_season_data[col].max()
        else:
            # Check for rows with data for the same 'Country' across all seasons
            country_data = df[(df['Country'] == country) & (~df[numeric_columns].isna().all(axis=1))]
            if len(country_data) > 0:
                for col in numeric_columns:
                    if pd.isna(row[col]):
                        row[col] = country_data[col].min()
            else:
                # Check for rows with data for the same 'Season' and 'Position' across all countries
                season_position_data = df[(df['Season'] == season) & (df['Position'] == position) & (~df[numeric_columns].isna().all(axis=1))]
                if len(season_position_data) > 0:
                    # Use the average of the lowest three values for each numeric column
                    for col in numeric_columns:
                        if pd.isna(row[col]):
                            lowest_three_values = season_position_data[col].nsmallest(3).mean()
                            row[col] = lowest_three_values
    
    return row

# Apply the fill_with_largest_or_lowest_or_average_of_3 function to each row
df_cleaned = df.apply(fill_with_largest_or_lowest_or_average_of_3, axis=1)

df_cleaned.to_csv(mean_data_file, index=False)

print(f"Cleaned mean data saved to {mean_data_file}")
print(df_cleaned)
