import os 
import csv

csv = election_data.csv

#Define Variables
totalvotecount = 0
canidate_list = []
Kahn_Vote_Count = 0 
Correy_Vote_Count = 0 
Li_Vote_Count = 0
OTooley_Vote_Count = 0

#ImportData

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    csv_dictionary = csv.DictReader(csv_file)

#Create List of Canidates
    for row in csv_reader:
        totalvotecount = totalvotecount +1 

    if row[2] not in canidate_list:
        canidate_list.append(row[2])

    if row[2] == canidate_list[0]:
        Kahn_Vote_Count = Kahn_Vote_Count + 1

    elif row[2] == canidate_list[1]:
        Correy_Vote_Count = Correy_Vote_Count + 1
    
    elif row[2] == canidate_list[2]:
        Li_Vote_Count = Li_Vote_Count + 1
    
    elif row[2] == canidate_list[3]:
        OTooley_Vote_Count = OTooley_Vote_Count + 1
    
    #print list 

