import pandas as pd

main_columns = ['Season', 'League',	'Team',	'Player', 'Nation',	'Pos',
                'Age','MP',	'Starts','Min',	'90s',	'Goals']
csv_files = ['Cleaned_Euro Squads and Stats.csv',
    'Cleaned_Defensive.csv',
    'Cleaned_Goal_and_shot.csv',
    'Cleaned_Goalkeeping.csv',
    'Cleaned_Passing_types.csv',
    'Cleaned_Passing.csv',
    'Cleaned_Possession.csv',
    'Cleaned_Shooting.csv']

for file in csv_files:
    file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\{file}'
    df = pd.read_csv(file_path)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.drop(columns=[col for col in main_columns if col in df.columns], errors='ignore')
    print(df)
    df.to_csv(file_path,index=False)

standard_file = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Player Data\Final Player Data\Cleaned_Standard_stats.csv'

st_df = pd.read_csv(standard_file)
st_df = st_df.loc[:, ~st_df.columns.str.contains('^Unnamed')]
st_df.to_csv(standard_file,index=False)