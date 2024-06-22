import pandas as pd
file_names = ['Cleaned_Euro Squads and Stats.csv',
    'Cleaned_Standard_stats.csv',
    'Cleaned_Defensive.csv',
    'Cleaned_Goal_and_shot.csv',
    'Cleaned_Goalkeeping.csv',
    'Cleaned_Passing_types.csv',
    'Cleaned_Passing.csv',
    'Cleaned_Possession.csv',
    'Cleaned_Shooting.csv']

for file_name in file_names:
   
    file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\{file_name}'
    
    df = pd.read_csv(file_path)

    # Create the 'Key' column by combining 'Season' and 'Player'
    df['Key'] = df.apply(lambda row: f"{row['Season']}_{row['Player']}", axis=1)
  
    # Remove apostrophes and white spaces from the Key column
    df['Key'] = df['Key'].str.replace("'", "").str.replace(" ", "")
    df['Season'] = df['Season'].str.replace("'", "").str.replace(" ", "")
   
    # Save the updated DataFrame back to the CSV
    df.to_csv(file_path, index=False)
    print(f"Updated {file_name}:")

