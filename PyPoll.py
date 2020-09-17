import os 
import csv

csv = os.path.join("Documents", "GitHub" "Python-Homework-Week-3","election_data.csv")

#Define Variables
totalvotecount = 0
canidate_list = []
Kahn_Vote_Count = 0 
Correy_Vote_Count = 0 
Li_Vote_Count = 0
OTooley_Vote_Count = 0

#ImportData

with open(csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

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

#calculate percentage of votes recieved
Kahn_Percentage = ("%.2f" % (Kahn_Vote_Count/totalvotecount*100))
Li_Percentage = ("%.2f" % (Li_Vote_Count/totalvotecount*100))
Correy_Percentage = ("%.2f" % (Correy_Vote_Count/totalvotecount*100))
OTooley_Percentage = ("%.2f" % (OTooley_Vote_Count/totalvotecount*100))

#winner 
if max(Kahn_Vote_Count, Correy_Vote_Count, Li_Vote_Count, OTooley_Vote_Count) == Kahn_Vote_Count:
    winner = 'Kahn'
elif max(Kahn_Vote_Count, Correy_Vote_Count, Li_Vote_Count, OTooley_Vote_Count) == Correy_Vote_Count:
    winner = 'Correy'
elif max(Kahn_Vote_Count, Correy_Vote_Count, Li_Vote_Count, OTooley_Vote_Count) == Li_Vote_Count:
    winner = "Li"
else: 
    winner = "O'Tooley"

#print 
print ("Election Results")
print ("---------------------------")
print (f"Total Votes: {totalvotecount}")
print ("---------------------------")
print(f"Kahn: {Kahn_Percentage}% {Kahn_Vote_Count}")
print(f"Correy: {Correy_Percentage}% {Correy_Vote_Count}")
print(f"Li: {Li_Percentage}% {Li_Vote_Count}")
print (f"O'Tooley: {OTooley_Percentage}% {OTooley_Vote_Count}")
print ("---------------------------")
print (f"Winner: {winner}")
print ("---------------------------")

#print list 
#print(output)
