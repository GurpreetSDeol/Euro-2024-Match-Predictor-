import pandas as pd 
from datetime import datetime


file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\New Data\All International results.csv'
Int_df = pd.read_csv(file_path) 



Country_dict = ['Albania', 'Andorra', 'Armenia', 'Austria', 'Belarus', 'Belgium', 'Bosnia',
 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'England', 'Estonia',
 'Finland', 'France', 'Georgia', 'Germany', 'Hungary', 'Iceland', 'Italy',
 'Kosovo', 'Latvia', 'Liechtenstein', 'Luxembourg', 'Moldova',
 'North Macedonia', 'Netherlands', 'Northern Ireland', 'Norway','Poland',
 'Portugal', 'Republic of Ireland', 'Romania', 'Russia', 'Scotland', 'Serbia',
 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine',
 'Wales']



# Function to parse dates with different formats
def parse_date(date_value):
    if isinstance(date_value, pd.Timestamp):
        return date_value
    for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
        try:
            return datetime.strptime(date_value, fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

def get_season(date):
    year = date.year
    previous_year = year - 1
    season = f"{previous_year}-{year}"
    return season


def determine_winner(row):
    if row['home_score'] > row['away_score']:
        return row['home_team']
    elif row['home_score'] < row['away_score']:
        return row['away_team']
    else:
        return 'Draw'

# Convert 'date' column using the custom parsing function
Int_df['date'] = Int_df['date'].apply(parse_date)

# Filter out rows with dates before 2017 and after 2024
filtered_df = Int_df[(Int_df['date'] >= datetime(2017, 1, 1)) & (Int_df['date'] <= datetime(2024, 6, 12))]


# Replace values in 'country' column
replace_dict = {'Czech Republic': 'Czechia', 'italy': 'Italy', 'Bosnia and Herzegovina':'Bosnia'}
filtered_df['home_team'] = filtered_df['home_team'].replace(replace_dict)
filtered_df['away_team'] = filtered_df['away_team'].replace(replace_dict)

unique_countries = pd.concat([filtered_df['home_team'], filtered_df['away_team']]).dropna().unique()

print(sorted(unique_countries))
set_Country_dict = set(Country_dict)
set_unique_countries = set(unique_countries)

# Find countries in Country_dict that are not in unique_countries
countries_not_in_unique = set_Country_dict - set_unique_countries

# Print countries not in unique_countries
print("Countries from Country_dict not in unique_countries:")
print(countries_not_in_unique)


#Include only European matches
Euro_df = filtered_df[(filtered_df['home_team'].isin(Country_dict)) & (filtered_df['away_team'].isin(Country_dict))].reset_index()

# Create 'Season' column based on 'date'
Euro_df['Season'] = Euro_df['date'].apply(get_season)

#Columns to drop 
drop_columns = ['tournament', 'city','country','neutral']
Euro_df = Euro_df.drop(columns=drop_columns)

Euro_df['result'] = Euro_df.apply(determine_winner, axis=1)

new_file_path = rf'C:\Users\gurpr\OneDrive\Documents\New Projects\Euros Match Predictor\Data\Final Data\Euros Data\Euro_Match_Results.csv'
Euro_df.to_csv(new_file_path)
#print(Euro_df)