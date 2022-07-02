import os
import csv
from numpy import average

# initialize the column lists
dateArr = []
plArr = []
compArr = []

# get the data source path
csvPath = os.path.join("Resources", "budget_data.csv")

# get the analysis results path
txtPath = os.path.join("Analysis", "results.txt")

# open the csv file
with open(csvPath, encoding="utf") as csvFile:
    
    # read the file contents
    csvReader = csv.reader(csvFile, delimiter=",")
    
    # advance the reader past the column headers
    csvHeader = next(csvReader)
    
    # iterate the reader through the remaining rows of the csv
    for row in csvReader:
        dateArr.append(row[0])
        plArr.append(int(row[1]))

# calculate the deltas within the profit/loss array
for i in range(len(plArr) - 1):
    compArr.append(plArr[i + 1] - plArr[i])

# part 1/5
totalMonths = len(dateArr)

# part 2/5
plSum = sum(plArr)

# part 3/5
plAverage = average(compArr)

# part 4/5
plMax = max(compArr)
dateMax = dateArr[compArr.index(plMax) + 1]

# part 5/5
plMin = min(compArr)
dateMin = dateArr[compArr.index(plMin) + 1]

# print the results to the terminal
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${plSum:,.2f}")
print(f"Average Change: ${plAverage:,.2f}")
print(f"Greatest Increase in Profits: {dateMax} (${plMax:,.2f})")
print(f"Greatest Decrease in Profits: {dateMin} (${plMin:,.2f})")

# write the results to a text file
with open(txtPath, "w") as txtFile:
    txtFile.write("Financial Analysis")
    txtFile.write("\n")
    txtFile.write("----------------------------------------")
    txtFile.write("\n")
    txtFile.write(f"Total Months: {totalMonths}")
    txtFile.write("\n")
    txtFile.write(f"Total: ${plSum:,.2f}")
    txtFile.write("\n")
    txtFile.write(f"Average Change: ${plAverage:,.2f}")
    txtFile.write("\n")
    txtFile.write(f"Greatest Increase in Profits: {dateMax} (${plMax:,.2f})")
    txtFile.write("\n")
    txtFile.write(f"Greatest Decrease in Profits: {dateMin} (${plMin:,.2f})")