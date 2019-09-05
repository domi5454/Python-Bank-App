#Domingo Rodriguez
#NWU Data Science Boot Camp
#Assignment 3 Python scripts
#2019-Fall

import os
import string
import csv
import math


#import csv and declare vars
fileName = "election_data.csv" #input("please enter the file name to open:")
filepath = os.path.join("..","Resources",fileName)
totalVotes = 0
winner = " "


voteList = []
candidatesDict = {"Khan":int(0),"Correy":int(0), "Li":int(0),"O'Tooley":int(0)}
writeIn = []
#import data
with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        voteList.append(row[2])
        if (str(row[2]) == "Khan"):
            candidatesDict["Khan"] += 1
        elif (str(row[2]) == "Correy"):
            candidatesDict["Correy"] += 1
        elif (str(row[2]) == "Li"):
            candidatesDict["Li"] += 1
        elif(str(row[2]) == "O'Tooley"):
            candidatesDict["O'Tooley"] +=1
        else:
            #in case of write in candidate vote
            writeIn.append(str(row[2]))
    totalVotes = len(voteList)

#determine max of popular votes
def maxVote(aDict):
    return max(aDict, key = lambda key:aDict[key])

#determine percentage of votes
def votePerct(anInt):
    votes = int(anInt)
    perct = round(float((votes/totalVotes)*100),2)
    return perct

#determine winner
def winnerFind(aDict):
   theWinner = str(maxVote(aDict))
   return theWinner

#winner - winnerFind(candidatesDict)
#print to console
winner = winnerFind(candidatesDict)
print(f"\n\n\nElection Results")
print(f"------------------------------------------------")
print(f"Total Votes:\t{totalVotes}")
print(f"------------------------------------------------")
print(f'Khan:\t{votePerct(int(candidatesDict["Khan"]))}%\t{candidatesDict["Khan"]}')
print(f'Correy:\t{votePerct(int(candidatesDict["Correy"]))}%\t{candidatesDict["Correy"]}')
print(f'Li:\t{votePerct(int(candidatesDict["Li"]))}%\t{candidatesDict["Li"]}')
print(f"O'Tooley:  "+str(votePerct(int(candidatesDict["O'Tooley"])))+"%\t"+str(candidatesDict["O'Tooley"]))
print(f"------------------------------------------------")
print(f"\n")
print(f"------------------------------------------------")
print(f"Winner:\t{winner}")
print(f"------------------------------------------------")
print("\n\n\n")

#print to text stream
fileOut = os.path.join("..","OutPut","Election_Analysis.txt")
with open(fileOut,"w",1,"UTF-8") as analysisOut:
    analysisOut.write("\n\n\nElection Results\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("Total Votes:\t"+str(totalVotes)+"\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write('Khan:\t'+str(votePerct(int(candidatesDict["Khan"])))+'%\t'+str(candidatesDict["Khan"])+'\n')
    analysisOut.write('Correy:\t'+str(votePerct(int(candidatesDict["Correy"])))+'%\t'+str(candidatesDict["Correy"])+'\n')
    analysisOut.write('Li:\t'+str(votePerct(int(candidatesDict["Li"])))+'%\t'+str(candidatesDict["Li"])+'\n')
    analysisOut.write("O'Tooley: "+str(votePerct(int(candidatesDict["O'Tooley"])))+'%\t'+str(candidatesDict["O'Tooley"])+'\n')
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.write("Winner:\t"+str(winner)+"\n")
    analysisOut.write("------------------------------------------------\n")
    analysisOut.close()
