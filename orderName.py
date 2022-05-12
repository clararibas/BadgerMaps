import csv
from operator import itemgetter

# Reading the CSV File
file = open('SampleTestFile.csv', encoding = "UTF-8")
reader = csv.DictReader(file)

# Print sorted name
for name in sorted(reader, key = itemgetter('First Name', 'Last Name')):
    if name['First Name'] == '':
        continue
    else:
        print(name['First Name'], name['Last Name'])