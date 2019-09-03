#Domingo Rodriguez
#NWU Data Science Boot Camp
#Assignment 3 Python scripts
#2019-Fall

import os
import string
import csv


filepath = os.path.join("..","Resources","budget_data.csv")
totalMths = 0
total = int(0)
budgetList = []


with open(filepath) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
       totalMths += 1 
       budgetList.append(
            {
                row[0]:row[1]

            }
        )
       total += int(row[1])
       rowSum = sum(int(row[1]))
#double check iterations
print(f"Total Months:\t{totalMths}\t\t{len(budgetList)}")
print(f"Total:\t{total}\t\t{rowSum}")

