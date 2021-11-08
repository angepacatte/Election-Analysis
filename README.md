                                                        #**_ Election-Analysis by County and Final Results_**##
##**Overview of the Election Audit**
  
  This election audit included looking at the 3 candidates and the breakdown of the votes for each candidate.   An analysis of the 3 counties involved in the election were also examined. Variables were created and code was written to determine the county with the largest vote turnout as well as which candidate won.  In Python, code was written with first opening the csv file and then writing code to work through the file to calculate and breakdown percentages by county and candidate.  
  
 This screenshot shows the different variables formulated.  Two examples are largest_county_count and largest_county_percent.
  
  
  <img width="1280" alt="Variables set" src="https://user-images.githubusercontent.com/85581208/140803981-6ba244e8-69fd-487c-a395-2e719a7d43aa.png">
  
  A preview of the code created to work through the rows to find the different counties and tally up their breakdown.
  <img width="1280" alt="Moving through the counties" src="https://user-images.githubusercontent.com/85581208/140805502-73fd8188-cc6a-413e-b459-f05d733b5e4f.png">  
  
  
  The results were compiled in the Election_Results.txt file.
  <img width="655" alt="Election_Results txt screenshot" src="https://user-images.githubusercontent.com/85581208/140805956-7af67532-19ca-42c8-ab99-475d250208c5.png">  

  
##**Election Audit Results**

* Total votes = 369,711
* Vote breakdown by county.  Percentage listed first with number of votes following.
  County Votes:
  Jefferson:  10.5%  38,855
  Denver:  82.8%  306,055
  Arapahoe:  6.7%  24,801
* Denver county had the most votes with a total of 306,055 which made up 82.8% of the votes.
* Candidate voting summary brokendown by percentage followed by number of votes in parentheses.  
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
* Diane DeGette was the winner of the election by a decisive number of 73.8% of the votes and a total of 272,892 votes.
  


##**Election Audit Summary**
  
  The purpose of creating this code was not only to use it for the current election analyzed but also to be able to apply it to any election.  The variables created would allow it to be applied to other csv files that contain election data.  The two places that would need to be modified would depend on where in the csv file the information is located.  See screenshot below where is it is locating where the county and candidate information is located.
![image](https://user-images.githubusercontent.com/85581208/140808731-44152d80-cf5c-41b8-b47e-f67ad7dd4b45.png)
 The rows are indexed according to where the candidate names and county names are in regards to the spreadsheet.  Those numbers would need to be modified so that the for loop would be looping in the right column.  
 
  Another modification would be at the very top of the script. The file_to_load and the file_to_save (at the top of the picture) would need to be specified for each file being opened and where the information obtained from the script is to be saved.
  ![image](https://user-images.githubusercontent.com/85581208/140809141-2bad9619-31cd-4d62-a0b0-5eafa59badd9.png) 
  
  Overall, it would be very easy to apply this code to different elections.  This application would save time and money.  Instrucions would just need to be made on where modifications would need to be made as the script is applied to different spreadsheet. 
  
  
