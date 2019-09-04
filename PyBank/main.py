#Domingo Rodriguez
#NWU Data Science Boot Camp
#Assignment 3 Python scripts
#2019-Fall

import os
import string
import csv
import math
import codecs

#import csv and declare vars
fileName = "budget_data.csv" #input("please enter the file name to open:")
filepath = os.path.join("..","Resources",fileName)
totalMths = 0
total = int(0)
budgetDict = {}

#delta changes
def findDelta(aDict):
    valList = list(aDict.values())
    deltaList = []
    for i in range(len(valList)):
        if i == len(valList)-1:
           break
        else:
            deltaList.append(int(valList[i+1]) - int(valList[i]))
       
    deltaSum = sum(deltaList)
    return float(deltaSum/(totalMths-1))

def findMax(aDict):
    keyList = list(aDict.keys())
    valList = list(aDict.values())
    maxVal = int(0)
    maxDate = " "
    for i in range(len(keyList)):
        if (int(valList[i]) > maxVal):
            maxDate = str(keyList[i])
            maxVal = int(valList[i])
    return maxDate+":  ($"+str(maxVal)+")"



def findMin(aDict):
    keyList = list(aDict.keys())
    valList = list(aDict.values())
    minVal = int(valList[0])
    minDate = " "
    for i in range(1, len(keyList)):
        if (int(valList[i]) < minVal):
            minDate = str(keyList[i])
            minVal = int(valList[i])
    return minDate+":  ($"+str(minVal)+")"

    
#import csv
with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    budgetDict = {date:amount for (date, amount) in reader}
    for amount in budgetDict.values():
        total += int(amount)
    totalMths = int(len(budgetDict))

maxProfit = findMax(budgetDict)
minProfit = findMin(budgetDict)
deltaProfit = round(findDelta(budgetDict), 2)
#print to console
print(f"\n\n\nFinancial Analysis")
print(f"------------------------------------------------")
print(f"Total Months:\t{totalMths}")
print(f"Total:\t${total}")
print(f"Average change:\t${str(deltaProfit)}")
print(f"Greatest Increase in Profits:\t{maxProfit}")
print(f"Greatest Decrease in Profits:\t{minProfit}")
print("\n\n\n\n")

#print to text file
fileOut = os.path.join("..","OutPut","Financial_Analysis.txt")
with open(fileOut,"w",1,"UTF-8") as analysisOut:
    analysisOut.write("\n\n\nFinancial Analysis\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("Total Months:\t"+str(totalMths)+"\n")
    analysisOut.write("Total:\t$"+str(total)+"\n")
    analysisOut.write("Average change:\t$"+str(deltaProfit)+"\n")
    analysisOut.write("Greatest Increase in Profits:\t"+str(maxProfit)+"\n")
    analysisOut.write("Greatest Decrease in Profits:\t"+str(minProfit)+"\n")
    analysisOut.close()
