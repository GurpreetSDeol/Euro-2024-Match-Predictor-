import pandas as pd

dtype = 'pred'

# List of match files
if dtype == 'build': 
    match_files = ['Euro_Match_Results.csv']
elif dtype == 'pred':
    match_files = [
        'Euro_2024_MatchUps.csv',
        'Euro_2024_R16_MatchUps.csv',
        'Euro_2024_QF_MatchUps.csv',
        'Euro_2024_SF_MatchUps.csv',
        'Euro_2024_F_MatchUps.csv'
    ]

# Numerical data file
numerical_file = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Team_Profile_By_Year_Data.csv'
numerical_df = pd.read_csv(numerical_file)

# Columns to convert to float
columns_to_convert = ['Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'Completed',
                      'Offside_pass', 'Blocked', 'Int Matches Played', 'Int Starts', 'Int Min',
                      'Int 90s', 'Int Goals', 'Int Assists', 'Int Non Penalty Goals', 
                      'Int Penalty Goals', 'Int Penaltes Attempted', 'Int Yellow Cards', 'Int Red Cards',
                      'Int Goals Per 90', 'Int Assists Per 90', 'Int Goals + Assits Per 90',
                      'Int Non Penalty Goals Per 90', 'Int Non Penalty Goals + Assits Per 90']

# Convert columns to float
for col in columns_to_convert:
    numerical_df[col] = pd.to_numeric(numerical_df[col], errors='coerce')

# Process each match file
for match_file in match_files:
    file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\{match_file}'
    matches_df = pd.read_csv(file_path)

    # Initialize an empty list to store dictionaries of match details with differences
    final_data = []

    # Iterate through rows in matches_df
    for index, row in matches_df.iterrows():
        home_team = row['home_team']
        away_team = row['away_team']
        season = row['Season']

        # Find corresponding rows in numerical_df
        home_row = numerical_df[(numerical_df['Country'] == home_team) & (numerical_df['Season'] == season)]
        away_row = numerical_df[(numerical_df['Country'] == away_team) & (numerical_df['Season'] == season)]

        if len(home_row) == 1 and len(away_row) == 1:
            home_matches_played = home_row['Int Matches Played'].values[0]
            away_matches_played = away_row['Int Matches Played'].values[0]

            # Check if 'Int Matches Played' is 0 or NaN for either team
            if pd.notna(home_matches_played) and pd.notna(away_matches_played) and home_matches_played > 0 and away_matches_played > 0:
                # Calculate differences for numerical float columns
                differences = {}
                for col in numerical_df.columns[2:]: 
                    if pd.api.types.is_numeric_dtype(numerical_df[col]):
                        home_value = home_row[col].values[0]
                        away_value = away_row[col].values[0]
                        differences[f'{col}_difference'] = (home_value - away_value)
                   
                # Create dictionary with match details and differences
                match_details = {
                    'Season': row['Season'],
                    'home_team': home_team,
                    'away_team': away_team,
                    'home_score': row['home_score'],
                    'away_score': row['away_score'],
                    'result': row['result'] 
                }
                match_details.update(differences)

                # Append to final_data list
                final_data.append(match_details)

    # Convert final_data list to DataFrame
    final_df = pd.DataFrame(final_data)

    # Save final_df to the appropriate CSV
    if dtype == 'build':
        output_file = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\{match_file.replace("_Results.csv", "_Team_Stats_Difference_per_Match.csv")}'
    elif dtype == 'pred':
        output_file = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\{match_file.replace("_MatchUps.csv", "_Team_Stats_Difference_per_Match.csv")}'
    
    final_df.round(3)
    final_df.to_csv(output_file, index=False)
    print(f"Saved merged data with differences to: {output_file}")

    # Display final_df (optional)
    print("\nFinal DataFrame with differences and result column:")
    print(len(final_df))
    print(final_df.columns)
na_percentage = final_df.isna().mean() * 100
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)     
pd.set_option('display.width', 1000)  

print(na_percentage)