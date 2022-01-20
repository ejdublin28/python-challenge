import os
import csv
from datetime import datetime
from statistics import mean

budget_csv = '/Users/emmadublin/Desktop/python-challenge/PyBank/Resources/budget_data.csv'
#budget_csv = os.path.join("..","Resources","budget_data.csv")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #total = 0
    #row_count = 0

    prof_loss = []
    date = []
    change = []
    for row in csvreader:
        #row_count += 1
        #total+= float(row[1])
        date.append(row[0])
        prof_loss.append(float(row[1]))

    print(f"Financial Analysis")
    print(f"------------------------------------------------------")
    print(f"Total Months: {len(date)}")
    print(f"Total: ${sum(prof_loss)}")

    #Adding 0 as change amount for the first month, so indices will align
    change.append(0)

    for i in range(1,len(prof_loss)):
        change.append(prof_loss[i] - prof_loss[i-1])   
    
        avg_chg = sum(change)/(len(change)-1)

        gr_inc = max(change)
        dt_gr_inc = date[change.index(gr_inc)]

        gr_dec = min(change)
        dt_gr_dec = date[change.index(gr_dec)]

    #These lines were used to check that change calculation worked correctly
    #print(len(change))
    #print(change)
 
    print(f"Average Change: ${round(avg_chg,2)}")
    print(f"Greatest Increase in Profits: {dt_gr_inc} (${gr_inc})")
    print(f"Greatest Decrease in Profits: {dt_gr_dec} (${gr_dec})")

output = [(f"Financial Analysis"),
(f"------------------------------------------------------"),
(f"Total Months: {len(date)}"),
(f"Total: ${sum(prof_loss)}"),
(f"Average Change: ${round(avg_chg,2)}"),
(f"Greatest Increase in Profits: {dt_gr_inc} (${gr_inc})"),
(f"Greatest Decrease in Profits: {dt_gr_dec} (${gr_dec})")]

# Set variable for output file
output_file = '/Users/emmadublin/Desktop/python-challenge/PyBank/analysis/financial_analysis.txt'
#output_file = os.path.join("..","Resources","financial_analysis.txt")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    datafile.write('\n'.join(output))
    
