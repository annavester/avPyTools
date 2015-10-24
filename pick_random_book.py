import csv
import random

with open('data/trimmed.csv') as csvfile:
  bookreader = [row for row in csv.reader(csvfile.read().splitlines())]
  line = random.choice(bookreader)
  author = line[2]
  title = line[1]
  print "Random book pick is %s by %s." % (title, author) 
