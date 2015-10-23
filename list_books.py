import csv
import random

with open('data/goodreads_library.csv', 'rU') as csvfile:
  bookreader = csv.DictReader(csvfile)
  for row in bookreader:
    print row['Title'], row['Author']
