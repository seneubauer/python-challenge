# python-challenge

## Problem
For the PyBank portion of this assignment we were asked to provide a quick statistical analysis of a bank's records. These records only included month/year timestamps corresponding with a profit or loss quantity.

For the PyPoll portion of this assignment we were asked to provide a quick evaluation of a small town's election results. The election data included a simple dataset with Voter ID, County, and Candidate as the categories.

## Goal
### PyBank Tasks (copied from assignment)
* Calculate the total number of months included in the dataset.
* Calculate the net total amount of "Profit/Losses" over the entire period.
* Calculate the changes in "Profits/Losses" over the entire period, and then the average of those changes.
* Calculate the greatest increase in profits.
* Calculate the greatest decrease in profits.
### PyPoll Tasks (copied from assignment)
* Calculate the total number of votes cast.
* Compile a complete list of candidates who received votes.
* Calculate the percentage of votes each candidate won.
* Determine the winner of the election based on popular vote.

## Setup
##### PyBank
The beginning of this script was to import relevant modules, define file paths, and initialize three lists. The middle of this script was dedicated to reading the contents of the data source file into two of the aforementioned lists. I had to take care to advance the csv reader past the source dataset's header. After those two lists were populated, I populated the third list with with the differences between the Profit/Losses list elements. This third list had to be one element shorter due to this method. The final section of this script simply reported the results to the terminal and saved the results to a text file using the same format.

##### PyPoll
The beginning of this script was to import relevant modules, defile file paths, and initialize six lists. The middle of this script was dedicated to reading the contents of the data source file into three of the aforementioned lists. I added a conditional statement to populate another list within the 'open with/for in' block. As with the previous script, I had to take care to advance the csv reader past the data source dataset's header. After these lists were populated, I had to collate the votes for each candidate into their own lists and calculate their percentages. The final section of this script performed the same function as the previous script: reporting to terminal and saving to text file.

## Execution Notes
These scripts yielded the same results as displayed in the homework assignment. I believe there is plenty of room for optimization but I am not proficient enough in Python to know what the upper limit is. The presence of multiple For loops iterating through similar lists makes me think there could be a clever way to combine them.

## Limitations
These scripts will only work if there is a data source file in the relative folders specified. These scripts were written with the assumption that each dataset column will be in a specific position and that there is a header. There is a 'black box' treatment of the data in the PyBank script, too. Intermediary lists are not reported when they could be useful to someone.