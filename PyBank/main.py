# Import Modules
import os
import csv

# Read File
csvpath=os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # save header as a list from 1st row, andvance one row
    
    months=1 # initialize months from 2nd row
    profitloss=float(next(csvreader)[1]) # initialize profitloss value from 2nd row, advance one row
    previous=profitloss # intialize previous value from 2nd row

    row3 = next(csvreader) # save 3rd row as a list, advance one row
    months+=1 # iterate months for 3rd row
    profitloss+=float(row3[1]) # iterate profitloss for 3rd row
    change=float(row3[1])-previous # calculate change from previous row
    previous=float(row3[1]) # update previous value from 3rd row
    changesum=change # initialize sum of changes from 3rd row
    minchange=change # initialize min change from 3rd row
    maxchange=change # initialize max change from 3rd row

    #loop through rest of the rows to make calculations
    for row in csvreader:
        months+=1
        profitloss+=float(row[1])
        change=float(row[1])-previous #change from the previous line
        previous=float(row[1])
        changesum+=change #sum of changes

        # Calculate min and max values for "change"
        if change>maxchange:
            maxchange=change
            maxmonth=row[0]
        elif change<minchange:
            minchange=change
            minmonth=row[0]
        
avg=changesum/(months-1)

output_file = os.path.join("output.txt")
with open(output_file, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"----------------------------------------------------\n")
    textfile.write(f"Total Months: {str(months)}\n")
    textfile.write(f"Total Profit/Losses: {'${:,.0f}'.format(profitloss)}\n")
    textfile.write(f"Average Change: {'${:,.2f}'.format(avg)}\n")
    textfile.write(f"Greatest Increase in Profits: {maxmonth} ({'${:,.0f}'.format(maxchange)})\n")
    textfile.write(f"Greatest Decrease in Profits: {minmonth} ({'${:,.0f}'.format(minchange)})\n") 
    textfile.write(f"----------------------------------------------------")
with open(output_file, 'r') as textfile:
    print(textfile.read())      