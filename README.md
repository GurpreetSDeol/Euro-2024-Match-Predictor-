# Euro-2024-Match-Predictor-
A  project about predicting the final winner of the 2024 Euros using RandomForest based on league player performance data collected from 2017/18  till today.

Instead of taking the usual approach of match statistics to make a predictor, I wanted to try using the data about national team players at club level instead. The basic approach is to create a national team profile for each european team per year, which contains atributes of various types of performance related data, such as tackles, goals, saves etc. Then for each match, find the difference between the profiles of the two teams ans use that to build two random forest models which predict how mnay goals each team may score. After a lot optamization, the final accuracy was about 55.21% and the predicted winner for the 2024 euros is Germany. 
This is assuming I have got the round of 16 teams correct as the format of the tournament is different this year. I will update the accuracy of each stage of the tournament as it progresses. 

#Overall Process


Firstly, I collected data about players from the most popular leagues in the world, then I collected the European National team lineups from 2016/2017 onwards. Since it would be impossible to get data for every single player for each national lineup, I combined these files together and filtered out the players I had no data for, which was a bigger issue for smaller european countries. The Team profile data was calculated using the mean of the players data however I ddi not want to use the data from GKs to factor into the performance of FWs for example. Therefore, since I had data for 7 positions, I calculated the mean for each Team, per Season, per Position. If any country had no data for a particular position, there were a few methods employed to work around that.

For the final step, for each attribute I chose the mean from the most appropriate position. For example, the data about savesper90 would be the mean value from the GK position, whereas the data for forwradpasses would be the average between the DF,MF and AM. Then for each match, the differnece between twp teams was calculated using the team profile for that year


#Overview of Files


The Data Processing folder contains 3 folders, meant to be used in the following order: Player Data Processing, Team Data Processing and Algorithm. The folders contain the python files used and a readme file explaing the order of the files.
The Data Folder contains all of the data, the new data contains files I found for the project and my collected data, some I used. The Final Data contains all the data used for the project.

This was my first major project so any feedback to improve this would be greatly appreciated. 
