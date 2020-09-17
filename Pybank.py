import os
import csv

csv = os.path.join("Documents", "GitHub", "Python-Homework-Week-3","budget_data.csv")

#Define Variables 
monthcount = 0
total_profit_loss = 0
previous_month = 0
greatest_increase = 0
greatest_decrease = 0
cumulative_increase_decrease = 0

#Import data
with open(csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

#Loop through rows, count, total and store increases/decreases
for row in csv_reader:
    monthcount = monthcount + 1
    total_profit_loss = total_profit_loss + int(row[1])
    current_month = int(row[1]) 
    increase_decrease = current_month - previous_month

#skip first row, averages issue 
if previous_month != 0:
    cumulative_increase_decrease =  cumulative_increase_decrease + increase_decrease

#increase and storing values
if increase_decrease > greatest_increase:
    greatest_increase = increase_decrease
    greatest_increase_month = row[0]
        
#decrease, if true, storing values
if increase_decrease < greatest_decrease:
    greatest_decrease = increase_decrease
    greatest_decrease_month = row[0]

#reset previous month     
previous_month = current_month

#calculate average loss/profit 
average_profit_loss = cumulative_increase_decrease / (monthcount - 1)

#change data types to be a little cleaner when I print
monthcount = int(monthcount)
total_profit_loss = int(total_profit_loss)
average_profit_loss = int(average_profit_loss)
greatest_increase = int(greatest_increase)
greatest_decrease = int(greatest_decrease)

#print list!!
