import pandas as pd
import time
import warnings

# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Start the timer
start_time = time.time()

# List of CSV file names to merge
main_file_path =  rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\Cleaned_Euro Squads and Stats.csv'
csv_files = ['Cleaned_Standard_stats.csv',
    'Cleaned_Defensive.csv',
    'Cleaned_Goal_and_shot.csv',
    'Cleaned_Goalkeeping.csv',
    'Cleaned_Passing_types.csv',
    'Cleaned_Passing.csv',
    'Cleaned_Possession.csv',
    'Cleaned_Shooting.csv'
]

# Function to clean the Key column
def clean_key_column(df):
    df['Key'] = df['Key'].astype(str).str.replace("'", "").str.replace(" ", "")
    return df

# Read and clean the main file
finaldf = pd.read_csv(main_file_path)
finaldf = clean_key_column(finaldf)

# Check if 'Int Min' column exists in finaldf and clean it if necessary
if 'Int Min' in finaldf.columns:
    finaldf = finaldf.dropna(subset=['Int Min'])  # Drop NaN first
    finaldf = finaldf[finaldf['Int Min'] != 0]    # Drop 0 values
    finaldf = finaldf[finaldf['Int Min'].astype(str).str.strip() != '']  # Drop empty strings
else:
    print("Column 'Int Min' not found in finaldf. Check column names.")

# Merge each additional file into finaldf

for file in csv_files:
    print(f"Merging data from {file}...")
    file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\{file}'
    df = pd.read_csv(file_path)
    df = clean_key_column(df)
    finaldf = pd.merge(finaldf, df, on='Key', how='left')

# Drop duplicate rows based on 'Key'
finaldf = finaldf.drop_duplicates(subset=['Key'])

# Drop rows where 'League' is NaN or empty
finaldf = finaldf.dropna(subset=['League'])
finaldf = finaldf[finaldf['League'].str.strip().astype(bool)]
    
replace_dict = {'larvia': 'Latvia', 'kosvo': 'Kosovo', 'italy': 'Italy'}

# Replace values in 'Country' column
finaldf['Country'] = finaldf['Country'].replace(replace_dict)

# Strip whitespace from 'Country' column
finaldf['Country'] = finaldf['Country'].str.strip()

# Capitalize country names
finaldf['Country'] = finaldf['Country'].str.capitalize()

# Define the mapping dictionary for a 'Position' Column

pos_mapping = {
    'GK': 'GK',
    'DF': 'DF',
    'MF': 'MF',
    'FW': 'FW',
    'MF,FW': 'AM',
    'FW,MF': 'AM',
    'MF,DF': 'DM',
    'DF,MF': 'DM',
    'DF,FW' : 'UK',
    'FW,DF' : 'UK'
}

# Create a new column based on the mapping
finaldf['Position'] = finaldf['Pos'].map(pos_mapping)

new_file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Merged_Unique_Dataset.csv'
finaldf.to_csv(new_file_path, index=False)

# End the timer and print the duration
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to run the code: {elapsed_time:.2f} seconds")
