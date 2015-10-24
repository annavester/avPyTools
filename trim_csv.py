import csv

reader = csv.DictReader(open("data/goodreads_library.csv"))
headers = {}
for h in reader.fieldnames:
  headers[h] = h

f = csv.DictWriter(open("data/trimmed.csv", "wb"), fieldnames = reader.fieldnames)
f.writerow(headers)

with open('data/goodreads_library.csv', 'rU') as csvfile:
  bookreader = csv.DictReader(csvfile)
  for row in bookreader:
    line = {}
    if 'to-read' in row['Exclusive Shelf']:
      for key, value in row.items():
        line[key] = value
      print line 
      f.writerow(line)
