# Import Modules
import os
import csv
import datetime

# Define Dictionary for state abreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Read File
csvpath=os.path.join("employee_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # read the original header and advance one line
    csv_header_out = [csv_header[0],'First Name','Last Name']+csv_header[2:] #create new header
    
    with open('csv_out.csv','w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2, delimiter=',')
        csvwriter.writerow(csv_header_out)
        for row in csvreader:
            names=row[1].split() #list with first and last name items
            dob=datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m-%d-%Y') #date in new date format
            #dob1=f"{row[2].split('-')[1]}-{row[2].split('-')[2]}-{row[2].split('-')[0]}"  #alternative expression without datetime import
            ssn_tr='***-**-'+row[3].split('-')[2] # trunkated ssn
            state=us_state_abbrev[row[4]] #lookup state abv in dictionary
            csvwriter.writerow([row[0],names[0],names[1],dob,ssn_tr,state])  #write line in output file
            

