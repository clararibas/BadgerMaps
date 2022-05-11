import csv
from operator import itemgetter
from datetime import datetime

# Reading the CSV File
file = open('SampleTestFile.csv', encoding="utf8")
reader = csv.DictReader(file)

#print sorted name
for name in sorted(reader, key=itemgetter('First Name', 'Last Name')):
    print(name['First Name'], name['Last Name'])