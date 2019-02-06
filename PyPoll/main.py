# Import Modules
import os
import csv

# Read File
csvpath=os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    #define starting values
    votes=0
    candidates={}
    winner=''
    winningvotes=0
    
    #loop through rows to make calculations
    csv_header = next(csvreader)
    for row in csvreader:
        votes+=1
        #populate dictionary for candidate/votes pair
        if row[2] not in candidates:
            candidates[row[2]]=1
        else:
            candidates[row[2]]=candidates[row[2]]+1

output_file = os.path.join("output.txt")
with open(output_file, 'w') as textfile:
    textfile.write(f"Election Results \n")
    textfile.write(f"-------------------------\n")
    textfile.write(f"Total Votes: {str(votes)}\n")
    textfile.write(f"-------------------------\n")
    for c in candidates:
        percentage=candidates[c]/votes
        textfile.write(f"{c}: {'{:,.3%}'.format(percentage)} ({str(candidates[c])})\n")
        if candidates[c]>winningvotes:
            winningvotes=candidates[c]
            winner=c
    textfile.write(f"-------------------------\n")
    textfile.write(f"Winner: {winner} \n")
    textfile.write(f"-------------------------")
with open(output_file, 'r') as textfile:
    print(textfile.read())      