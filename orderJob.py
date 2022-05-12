import csv
from operator import itemgetter

# Reading the CSV File
file = open('SampleTestFile.csv', encoding="utf8")
reader = csv.DictReader(file)

# Print sorted job
for job in sorted(reader, key=itemgetter('Job')):
    if job['Job'] == '':
        continue
    else:
        if job['Company'] == 'Badger Maps':
            print(job['Job'])