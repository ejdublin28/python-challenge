import os
import csv

election_csv =  '/Users/emmadublin/Desktop/python-challenge/PyPoll/Resources/election_data.csv'
#election_csv = os.path.join("..","Resources","election_data.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    #print(csvreader)

    csv_header = next(csvreader)

    voter_id = []
    county = []
    candidates = []
    vote_dict = {}
    perc = []

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

        vote_dict[row[2]] = vote_dict.get(row[2],0)+1
    #print(vote_dict)

    #Getting total votes
    vote_count = len(voter_id)
    #print(f"Total Votes: {vote_count}")
    
    can = list(vote_dict.keys())
    counts = list(vote_dict.values())

    for i in range(0,len(can)):
        perc.append('{:.3f}%'.format((counts[i]/vote_count)*100))
    #print(perc)

    #Print Header
    header = (f'''Election Results\n------------------------------\nTotal Votes: {vote_count}\n------------------------------\n''')

    print(header)
    
    detail = []
    #Print Candidate Detail
    for i in range(0,len(can)):
       print(f"{can[i]}: {perc[i]} ({counts[i]})")
       detail.append((f"{can[i]}: {perc[i]} ({counts[i]})"))

    #Print Footer
    footer = (f'''\n------------------------------\nWinner: {max(vote_dict,key = vote_dict.get)}\n------------------------------''')
    print(footer)

# Set variable for output file
output_file = '/Users/emmadublin/Desktop/python-challenge/PyPoll/analysis/election_results.txt'
#output_file = os.path.join("..","Resources","election_results.txt")
#Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    datafile.write((header))
    datafile.write('\n'.join(detail))
    datafile.write((footer))