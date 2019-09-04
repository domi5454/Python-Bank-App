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
fileName = "election_data.csv" #input("please enter the file name to open:")
filepath = os.path.join("..","Resources",fileName)
totalVotes = 0
winner = " "

electionDict = {}
    
#import data
with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    electionDict = {voterID:[county, candidate] for (voterID, county, candidate) in reader}
    totalVotes = len(electionDict)
    
#count votes per candidate
#def candidateCount(aList)
#determine percentage of votes
#def votePerct(aList)
#determine winner
#def winnerFind(aList/aSet)

#print to console
print(f"\n\n\nElection Results")
print(f"------------------------------------------------")
print(f"Total Votes:\t{totalVotes}")
print(f"------------------------------------------------")

print(f"------------------------------------------------")

print(f"------------------------------------------------")
print(f"Winner:\t{winner}")
print(f"------------------------------------------------")
print("\n\n\n\n")

#print to text stream
fileOut = os.path.join("..","OutPut","Election_Analysis.txt")
with open(fileOut,"w",1,"UTF-8") as analysisOut:
    analysisOut.write("\n\n\nElection Results\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("Total Votes:\t"+str(totalVotes)+"\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("\n\n\n\n\n\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("Winner:\t"+str(winner)+"\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.close()
