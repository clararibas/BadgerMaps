import csv
from operator import itemgetter
from datetime import datetime

# Reading the CSV File
file = open('SampleTestFile.csv', encoding="utf8")
reader = csv.DictReader(file)

#print sorted job
for job in sorted(reader, key=itemgetter('Job')):
    if job['Company'] == 'Badger Maps':
        print(job['Job'])