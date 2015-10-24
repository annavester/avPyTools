import csv

with open('data/trimmed.csv', 'rU') as csvfile:
  bookreader = csv.DictReader(csvfile)
  for row in bookreader:
    print row['Title'], row['Author']
