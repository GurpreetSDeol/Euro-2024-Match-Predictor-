# Euro-2024-Match-Predictor

A project aimed at predicting the winner of the 2024 Euros using a Random Forest model based on league player performance data collected from the 2017/18 season to the present.

## Project Overview
Rather than using traditional match statistics to build a predictor, this project utilizes data on national team players at the club level. The core idea is to create a national team profile for each European team annually, incorporating various performance-related attributes such as tackles, goals, saves, etc. For each match, the difference between the profiles of the two teams is calculated and used to build two Random Forest models that predict the number of goals each team might score. After extensive optimization, the model achieved an accuracy of approximately 55.21%, predicting Germany as the winner of the 2024 Euros. This prediction assumes the correct identification of the round of 16 teams, considering the tournament's unique format this year. The accuracy will be updated as the tournament progresses.

## Overall Process

#### Data Collection:

Gathered player data from major global leagues.

Collected European National team lineups from 2016/2017 onwards.

Filtered out players with no available data, which posed a greater challenge for smaller European countries.

#### Team Profile Calculation:

Calculated team profiles using the mean performance data of players by position, excluding goalkeepers (GKs) when evaluating forwards (FWs) and vice versa.
Averaged data for each team, per season, per position, employing specific methods to handle missing data for any position.


#### Attribute Selection:

Selected the mean value for each attribute from the most relevant position (e.g., saves per 90 minutes from GKs, forward passes from a combination of defenders (DF), midfielders (MF), and attacking midfielders (AM)).

Calculated the difference between the team profiles for each match.

## Folder Structure

#### Data Processing

#### Player Data Processing

Normalize_Names.py: Fix encoding issues with team and player names across all data files to prepare for merging.

CreateKey.py: Create a unique key for each player per season to use as the merging column.

DeleteColumns.py: Drop any duplicate columns from all files except for one.

MergeData.py: Combine player performance statistics with matching players for each national team by season and add a new Position column.

#### Team Data Processing

ResultsSorter.py: Create a DataFrame containing only European international matches.

Mean_Calculator.py: Calculate the mean for every numeric column grouped by position, per country, per season.

Clean_Mean_File.py: Deal with any missing values after the mean calculation with appropriate methods.

Position_Per_Column.ipynb: Identify the top 2 positions with the highest value for each column.

Team_Profile_By_Year.py: For each team per season, combine data for each column from the most relevant position, such as save% data from GK only.

Difference_Calculator.py: Calculate the difference in stats for that season between each team in each match using the team profile data.

#### Algorithm

Algorithm_Data_Preparation.py: Prepare the data for the algorithm.

RandomForest_Algorithm.ipynb: Build and optimize the Random Forest models.

Data: Contains all the data processed from Algorithm_Data_Preparation.py.

#### Data

Contains the original and processed data sorted in various folders.

#### Final Predictions

Final_Predictions.csv: The final predictions for the 2024 Euros.


#### This was my first major project, and I welcome any feedback for improvement.
