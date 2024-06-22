import pandas as pd
import numpy as np

# Define position mapping for all numerical columns
position_mapping = {'Age': ['GK', 'DF', 'MF', 'FW', 'DM', 'AM', 'UK'],
'MP': ['GK', 'DF', 'MF', 'FW', 'DM', 'AM', 'UK'],
'Starts': ['GK', 'DF', 'MF', 'FW', 'DM', 'AM', 'UK'],
'90s': ['GK', 'DF', 'MF', 'FW', 'DM', 'AM', 'UK'],
'Int Matches Played': 'FW',
'Int Starts': 'FW',
'Int Min': 'FW',
'Int 90s': 'FW',
'Int Goals': 'FW',
'Int Assists': 'AM',
'Int Non Penalty Goals': 'FW',
'Int Penalty Goals': 'AM',
'Int Penaltes Attempted': 'AM',
'Int Yellow Cards': 'DF',
'Int Red Cards': '[DF,DM]',
'Int Goals Per 90': 'FW',
'Int Assists Per 90': 'FW',
'Int Goals + Assits Per 90': '[FW,AM',
'Int Non Penalty Goals Per 90': 'FW',
'Int Non Penalty Goals + Assits Per 90': '[FW,AM',
'Goals': 'FW',
'Assists': '[AM,MF]',
'GoalsandAssists': '[FW,AM]',
'NonPenaltyGoals': 'FW',
'PenaltyGoals': 'FW',
'PenaltiesAttemped': 'FW',
'YelloCards': '[DF,DM]',
'RedCards': 'DF',
'PrgC': '[AM,MF,UK,FW]',
'ProgressiveCarries_x': '[DM,MF]',
'ProgressivePasses': '[UK,DM,MF',
'GoalsPer90': 'FW',
'AssistPer90': '[FW,AM',
'GoalsandAssistPer90': '[FW,MF,AM]',
'NonPenaltyGoalsPer90': 'FW',
'Total_Tackles': '[DM,DF,MF]',
'Tackles_Won': '[DF,MF]',
'Tackles_Def_3rd': '[DF,DM,MF]',
'Tackles_mid_3rd': 'MF',
'Tackles_Att_3rd': 'FW',
'Drib_Tackled': 'MF',
'Drib_Tackle_Lost': 'MF',
'Total_Blocks': 'MF',
'Shots_Blocked': 'DF',
'Passes_Blocked': '[DM,MF]',
'Interceptions': 'DF',
'Clearance': 'DF',
'Errors_to_shot': '[DF,GK]',
'SCA': '[DM,AM,FW]',
'SCA90': '[DM,AM,FW]',
'PassLive': '[MF,AM]',
'PassDead': '[AM,MF]',
'TO': 'UK',
'Sh': 'FW',
'Fld': 'FW',
'Def': 'DM',
'GCA': 'FW',
'GCA90': '[FW,AM]',
'GA': 'GK',
'GA90': 'GK',
'SoTA': 'GK',
'Saves': 'GK',
'Save%': 'GK',
'W': 'GK',
'D': 'GK',
'L': 'GK',
'CS': 'GK',
'CS%': 'GK',
'PKatt_x': 'GK',
'PKA': 'GK',
'PKsv': 'GK',
'Save%.1': 'GK',
'Live': '[MF,AM]',
'Dead': '[MF,AM]',
'FK': '[MF,AM,FW]',
'TB': '[DM,MF,AM]',
'Sw': 'DM',
'Crs': '[DM,MF]',
'TI': 'DF',
'CK': '[DM,MF]',
'Completed': '[DM,MF,AM]',
'Offside_pass': 'DM',
'Blocked': 'UK',
'Cmp': 'DM',
'Att': 'DM',
'Cmp%': 'FW',
'TotDist_x': 'DM',
'PrgDist': 'MF',
'SP_Cmp': 'UK',
'SP_Att': 'UK',
'SP_Cmp%': 'FW',
'MP_Cmp': 'DM',
'MP_Att': 'DM',
'MP_Cmp%': 'FW',
'LP_Cmp': 'GK',
'LP_Att': 'GK',
'LP_Cmp%': 'DM',
'Touches': 'DM',
'TouchesDef Pen': 'GK',
'TouchesDef 3rd': 'GK',
'TouchesMid 3rd': 'DM',
'TouchesAtt 3rd': '[UK,MF,FW]',
'TouchesAtt Pen': 'FW',
'TouchesLive': 'DM',
'DribblesAtt': '[UK,MF,AM]',
'DribbleSucc': '[UK,MF,AM]',
'DribbleSucc%': '[AM,FW]',
'DribbleTkld': 'FW',
'Carries': 'DF',
'TotDist_y': 'DM',
'ProgressivegDist': 'DM',
'ProgressiveCarries_y': '[DM,MF,AM]',
'ProgressiveFinalThird': '[DF,MF,AM]',
'CarriesPenArea': 'FW',
'Miscontrolled': 'AM',
'Dispossed': '[AM,FW]',
'Recievd ': 'DM',
'ProgressiveReceive': '[AM,FW,UK]',
'Shots': 'FW',
'ShotsOnTarget': 'FW',
'SoT%': 'MF',
'Sh/90': 'FW',
'SoT/90': 'AM',
'GoalsPerShot': '[AM,FW]',
'GoalsPerShotOnTarget': '[AM,FW',
'AvgShotDistance': '[AM,FW]',
'GoalsFromPenalties': 'FW',
'PKatt_y': 'FW'}
# Load the final difference data from CSV
final_difference_file =  r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Mean_Country_Data.csv'
df = pd.read_csv(final_difference_file)

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


# Function to get the highest value or average of values based on position mapping
def get_value_based_on_position(group, column, positions):
    if isinstance(positions, list):
        values = group[group['Position'].isin(positions)][column].dropna()
        return values.mean() if not values.empty else np.nan
    else:
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

# Round the numerical values to 2 decimal places


# Sort the DataFrame by 'Season' first, then by 'Country'
grouped_df.sort_values(by=['Season', 'Country'], inplace=True)

# Display the grouped DataFrame
print("Grouped DataFrame with selected values:")
print(grouped_df)

# Save the grouped DataFrame to a new CSV file
file_path =  r'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Team_Profile_By_Year_Data.csv'
grouped_df.to_csv(file_path, index=False)
print(len(grouped_df))
print(f"Saved grouped data to: {file_path}")

