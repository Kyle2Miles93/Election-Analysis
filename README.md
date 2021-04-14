# Election_Analysis

## Election Audit Project Overview 

  I reviewed election results for a Colorado congressional election using Python programming.
I used **Python: Version 3.7.6** to automate the analysis of the election. In my script, I calculated:

1. The total number of votes cast
2. The vote count for each candidate
3. The percentage of votes each candidate received.
4. The winner of the election
  - the winner's vote total and percentage of the vote
  
5. I then wrote a script that automated writing to a text file the results of the election
6. I did the same for all the counties: which county received the most votes
and the percentages of the vote total each county received.

All this to analyze which counties and which constituents vote for whom.

## Resources

- Software: Python 3.7.6
- Data Source: election_results.csv
- Visual Code Editor 1.51.1

## Election Audit Results

The analysis of the election shows:

 - there were 369,711 total votes cast in the congressional election.
 
   - Charles Casper Stockham received 85,213 votes and 23.0% of the total
   - Diana Degette received 272,892 votes and 73.8% of the total
   - *and* Raymon Anthony Doane received 11,606 votes and 3.1% of the total
 
 - The winner of election was:
   ### Diana Degette with 73.8% of the vote and 272,892 votes.

for each county in the precinct:

- Jefferson County received 38,855 votes with 10.5% of the votes.
- Denver county received 306,055 votes with 82.8% of the votes.
- Araphoe county received 24,801 votes with 6.7% of the votes.

### The county with the largest turnout in the precinct was **Denver**.

## Election Audit Summary

Here are some screenshots of my code for the election audit:

![VS Code](https://github.com/Kyle2Miles93/Election-Analysis/blob/main/Resources/Code_VS_1.png)

![VS Code second half](https://github.com/Kyle2Miles93/Election-Analysis/blob/main/Resources/Code_VS_2.png)

Here is a screenshot of my text file that was written through my python code:

![Election_analysis_text file](https://github.com/Kyle2Miles93/Election-Analysis/blob/main/Resources/Election_analysis_%20txt.png)

This script can be used for other election audits. It enables one to easily write text automatically to a separate file on *Visual Studio
Code* or other software with **Python**. It is a script that calculates the percentage of the votes had for each county and candidate, as well
as the total vote counts for each candidate and county and finally the total votes cast. It displays all of the necessay data for analysis
in an easy-to-read format, taken from a large list of data from an CSV spreadsheet. I propose that other businesses use this script for the following reasons:

1. The script can write to a separate text file and analyze the results *simultaneously*.
2. The script can calculate the necessary analytics automatically and efficiently, like
 - percentage of votes
 - candidates' vote totals
 - the winner of the election as well as 
 - the largest voter turnout

Any business can benefit from this type of analysis. It can be modified further to help with analysis of other elections by:

1. changing the repetition statements to check for different attributes of an election spreadsheet with more categories
2. adding more variables (possibly more **lists** or **dictionaries**) to hold values for each of these additional attributes.
3. Python has functionalities to read from a csv file, if writing to a brand-new sheet isn't totally necessary.





