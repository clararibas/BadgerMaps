import csv
from datetime import datetime

# Reading the CSV File
file = open('SampleTestFile.csv', encoding="utf8")
reader = csv.DictReader(file)

# Making a list with the dates
dates = []
for col in reader:
    if col['Last Check-In Date'] == '':
        continue
    else:
        dates.append(col['Last Check-In Date'])

# Sorting the dates list
dates.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))

# Locate the user with the earliest date
file = open('SampleTestFile.csv', encoding="utf8")
reader = csv.DictReader(file)

for line in reader:
    if line['Last Check-In Date'] == dates[0]:
        print(line['First Name'], line['Last Name'],'has the earliest check in date:', dates[0])


