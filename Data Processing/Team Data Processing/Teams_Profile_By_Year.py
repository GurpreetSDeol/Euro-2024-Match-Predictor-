import pandas as pd
import numpy as np

# Load your DataFrame from the CSV file
file_path = r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Mean_Country_Data.csv'
df = pd.read_csv(file_path)

# Define position mapping for all numerical columns
position_mapping = {
    '90s':['GK', 'DM'],
'Age':['GK', 'DF'],
'AssistPer90':['DM', 'AM'],
'Assists':['FW', 'AM'],
'Att':['DF', 'DM'],
'AvgShotDistance':['MF', 'DM'],
'Blocked':['DM', 'MF'],
'CK':['AM', 'MF'],
'CS':['GK'],
'CS%':['GK'],
'Carries':['DF', 'DM'],
'CarriesPenArea':['FW'],
'Clearance':['DF'],
'Cmp':['DF', 'DM'],
'Cmp%':['DF', 'DM'],
'Completed':['DF', 'DM'],
'Crs':['AM', 'DM'],
'D':['GK'],
'Dead':['GK'],
'Def':['MF'],
'Def.1':['MF'],
'Dispossed':['FW', 'AM'],
'Drib_Tackle_Lost':['MF'],
'Drib_Tackled':['DM', 'DF'],
'DribbleSucc':['AM', 'FW'],
'DribbleSucc%':['GK'],
'DribbleTkld':['FW', 'AM'],
'DribblesAtt':['AM', 'FW'],
'Errors_to_shot':['GK'],
'FK':['GK'],
'Fld':['FW'],
'Fld.1':['FW'],
'GA':['GK'],
'GA90':['GK'],
'GCA':['FW', 'AM'],
'GCA90':['AM', 'FW'],
'Goals':['FW'],
'GoalsFromPenalties':['FW'],
'GoalsPer90':['FW'],
'GoalsPerShot':['FW'],
'GoalsPerShotOnTarget':['FW', 'AM'],
'GoalsandAssistPer90':['DM', 'MF'],
'GoalsandAssists':['FW'],
'Int 90s':['GK', 'DF'],
'Int Assists':['FW', 'AM'],
'Int Assists Per 90':['FW'],
'Int Goals':['FW'],
'Int Goals + Assists ':['FW'],
'Int Goals + Assits Per 90':['FW'],
'Int Goals Per 90':['FW'],
'Int Matches Played':['GK', 'DM'],
'Int Min':['GK', 'DF'],
'Int Non Penalty Goals':['FW'],
'Int Non Penalty Goals + Assits Per 90':['FW', 'AM'],
'Int Non Penalty Goals Per 90':['FW'],
'Int Penaltes Attempted':['FW'],
'Int Penalty Goals':['FW'],
'Int Red Cards':['DM', 'DF'],
'Int Starts':['GK', 'DF'],
'Int Yellow Cards':['DM', 'DF'],
'Interceptions':['DF', 'DM'],
'L':['GK'],
'LP_Att':['GK'],
'LP_Cmp':['GK'],
'LP_Cmp%':['MF', 'DF'],
'Live':['DF', 'DM'],
'MP':['GK', 'DM'],
'MP_Att':['DF', 'DM'],
'MP_Cmp':['DF', 'DM'],
'MP_Cmp%':['GK', 'DF'],
'Min':['GK', 'DM'],
'Miscontrolled':['FW'],
'NonPenaltyGoals':['FW'],
'NonPenaltyGoalsPer90':['FW', 'AM'],
'Offside_pass':['MF', 'DM'],
'PKA':['GK'],
'PKatt_x':['GK'],
'PKatt_y':['FW'],
'PKsv':['GK'],
'PassDead':['AM', 'MF'],
'PassDead.1':['AM', 'DM'],
'PassLive':['MF', 'AM'],
'PassLive.1':['FW', 'AM'],
'Passes_Att':['DF', 'DM'],
'Passes_Blocked':['MF', 'DM'],
'PenaltiesAttemped':['FW'],
'PenaltyGoals':['FW'],
'PrgC':['AM', 'FW'],
'PrgDist':['GK'],
'ProgressiveCarries_x':['MF', 'DM'],
'ProgressiveCarries_y':['AM', 'FW'],
'ProgressiveFinalThird':['AM', 'DM'],
'ProgressivePasses':['FW', 'AM'],
'ProgressiveReceive':['FW', 'AM'],
'ProgressivegDist':['DF', 'DM'],
'Recievd ':['DM', 'DF'],
'RedCards':['DM', 'DF'],
'SCA':['AM', 'FW'],
'SCA90':['AM', 'FW'],
'SP_Att':['DM', 'DF'],
'SP_Cmp':['DM', 'DF'],
'SP_Cmp%':['GK', 'DF'],
'Save%':['DF', 'GK'],
'Save%.1':['GK'],
'Saves':['GK'],
'Sh':['FW'],
'Sh.1':['FW'],
'Sh/90':['FW'],
'Shots':['FW'],
'ShotsOnTarget':['FW'],
'Shots_Blocked':['DF'],
'SoT%':['FW', 'AM'],
'SoT/90':['FW'],
'SoTA':['GK'],
'Starts':['GK', 'DF'],
'Sw':['MF', 'DF'],
'TB':['MF', 'AM'],
'TI':['DF', 'DM'],
'TO':['FW', 'AM'],
'TO.1':['FW'],
'Tackles_Att_3rd':['MF', 'DM'],
'Tackles_Def_3rd':['DM', 'DF'],
'Tackles_Won':['DM', 'MF'],
'Tackles_mid_3rd':['MF', 'DM'],
'TotDist_x':['DF', 'GK'],
'TotDist_y':['DM', 'DF'],
'Total_Blocks':['DM', 'MF'],
'Total_Tackles':['DM', 'MF'],
'Touches':['DF', 'DM'],
'TouchesAtt 3rd':['FW', 'AM'],
'TouchesAtt Pen':['FW'],
'TouchesDef 3rd':['GK'],
'TouchesDef Pen':['GK'],
'TouchesLive':['DF', 'DM'],
'TouchesMid 3rd':['DM', 'MF'],
'W':['GK'],
'Year':['DM', 'FW'],
'YelloCards':['DM', 'MF']
}

# Columns to convert to float (if necessary)
columns_to_convert = [
    'Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'Completed',
    'Offside_pass', 'Blocked', 'Int Matches Played', 'Int Starts', 'Int Min',
    'Int 90s', 'Int Goals', 'Int Assists', 'Int Non Penalty Goals',
    'Int Penalty Goals', 'Int Penaltes Attempted', 'Int Yellow Cards', 'Int Red Cards',
    'Int Goals Per 90', 'Int Assists Per 90', 'Int Goals + Assits Per 90',
    'Int Non Penalty Goals Per 90', 'Int Non Penalty Goals + Assits Per 90'
]

# Convert specified columns to float (if necessary)
for col in columns_to_convert:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Function to get the highest value or average of values based on position mapping
def get_value_based_on_position(group, column, positions):
    if isinstance(positions, list):
        # First try to get the value from the specified positions
        values = group[group['Position'].isin(positions)][column].dropna()
        if not values.empty:
            return values.mean()
        
        # If no values found for specified positions, get the next highest value for the same country and season
        other_values = group[group['Position'].notna() & ~group['Position'].isin(positions)][column].dropna()
        if not other_values.empty:
            return other_values.max()
        
        # If no values found at all, return NaN
        return np.nan
    else:
        # Fallback case if positions are not a list
        values = group[column].dropna()
        return values.max() if not values.empty else np.nan

# Group by 'Country', 'Season' and apply the aggregation
result = []
for (country, season), group in df.groupby(['Country', 'Season']):
    row = {'Country': country, 'Season': season}
    for column, positions in position_mapping.items():
        row[column] = get_value_based_on_position(group, column, positions)
    result.append(row)

# Create DataFrame from result
grouped_df = pd.DataFrame(result)

# Save the grouped DataFrame to a new CSV file
file_path =  r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Team_Profile_By_Year_Data.csv'
grouped_df.to_csv(file_path, index=False)
print(len(grouped_df))
print(f"Saved grouped data to: {file_path}")

# Round the numerical values
na_percentage = grouped_df.isna().mean() * 100
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)     
pd.set_option('display.width', 1000)  

print(na_percentage)

