1) Normalize_Names.py: Fix any encoding issues with team and player names across all data files to prepeare for merging
2) CreateKey.py: Create a unique key for each player per season to use as the merging column 
3) DeleteColumns.py: Drop any dupliactae columns from all files except for one. 
4) MergeData.py: Combine player performance statistics with matching players for each national team by season and add a new POsition column