import pandas as pd
import chardet
import unicodedata


#Run it seperatly for   'Fixed_Euro Squads and Stats.csv' by changing 'Team' to 'Country'
file_names = [
    'Standard_stats.csv',
    'Defensive.csv',
    'Goal_and_shot.csv',
    'Goalkeeping.csv',
    'Passing_types.csv',
    'Passing.csv',
    'Possession.csv',
    'Shooting.csv']

#file_names = ['Euro Squads and Stats.csv']

def normalize_name(name):
    if isinstance(name, str):
        # Remove diacritical marks
        name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('ASCII')
        # Convert to lower case (or upper case if preferred)
        name = name.lower()
    return name

for file_name in file_names:
    # Detect file encoding
    file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Original Player Data\{file_name}'
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f'Detected encoding for {file_name}: {encoding}')
    
    # Read the CSV file with the detected encoding
    df = pd.read_csv(file_path, encoding=encoding)
    

    if 'Season' not in df.columns:
          df['Season'] = df['Year'].apply(lambda year: f"{year - 1}-{year}")   


    # Normalize the 'Team' and 'Player' columns
    for col in ['Team', 'Player']:
        df[col] = df[col].apply(normalize_name)
    
    # Remove rows where 'Player' is 'Squad Total' or 'Opponent Total'
   
    df = df[~df['Player'].isin(['squad total', 'opponent total'])]
    
   
    normalized_file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\Cleaned_{file_name}'
    df.to_csv(normalized_file_path, index=False, encoding='utf-8')
    
    print(f"Processed and saved: {normalized_file_path}")

print("All files processed.")
