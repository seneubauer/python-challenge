import os
import csv

# initialize the column lists
voterID = []
county = []
candidates = []
uniqueCandidates = []
uniqueCandidatesVotes = []
uniqueCandidatesPercents = []

# get the data source path
csvPath = os.path.join("Resources", "election_data.csv")

# get the election results path
txtPath = os.path.join("Analysis", "results.txt")

# open the csv file
with open(csvPath, encoding="utf") as csvFile:
    
    # read the file contents
    csvReader = csv.reader(csvFile, delimiter=",")
    
    # advance the reader past the column headers
    csvHeader = next(csvReader)
    
    # iterate the reader through the remaining rows of the csv
    for row in csvReader:
        voterID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
        # part 2/5
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

# part 1/5
totalVotes = len(voterID)

# part 3+4/5
count = 0
for i in range(len(uniqueCandidates)):
    count = candidates.count(uniqueCandidates[i])
    uniqueCandidatesVotes.append(count)
    uniqueCandidatesPercents.append(count / totalVotes)

# get first place winner based on highest percentage
firstVotes = max(uniqueCandidatesVotes)
firstIndex = uniqueCandidatesVotes.index(firstVotes)
firstName = uniqueCandidates[firstIndex]

# print the results to the terminal
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {totalVotes:,}")
print("----------------------------------------")
for i in range(len(uniqueCandidates)):
    print(f"{uniqueCandidates[i]}: {uniqueCandidatesPercents[i]:.3%} ({uniqueCandidatesVotes[i]:,})")
print("----------------------------------------")
print(f"Winner: {firstName}")
print("----------------------------------------")

# write the results to a text file
with open(txtPath, "w") as txtFile:
    txtFile.write("Election Results")
    txtFile.write("\n")
    txtFile.write("----------------------------------------")
    txtFile.write("\n")
    txtFile.write(f"Total Votes: {totalVotes:,}")
    txtFile.write("\n")
    txtFile.write("----------------------------------------")
    txtFile.write("\n")
    for i in range(len(uniqueCandidates)):
        txtFile.write(f"{uniqueCandidates[i]}: {uniqueCandidatesPercents[i]:.3%} ({uniqueCandidatesVotes[i]:,})")
        txtFile.write("\n")
    txtFile.write("----------------------------------------")
    txtFile.write("\n")
    txtFile.write(f"Winner: {firstName}")
    txtFile.write("\n")
    txtFile.write("----------------------------------------")