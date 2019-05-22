# -*- coding: utf-8 -*-
import csv

# Global array of unique phone numbers
uniqueNumbers = []

with open('texts.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  calls = list(reader)

for row in texts:
  if row[0] not in uniqueNumbers:
    uniqueNumbers.append(row[0])

  if row[1] not in uniqueNumbers:
    uniqueNumbers.append(row[1])

for row in calls:
  if row[0] not in uniqueNumbers:
    uniqueNumbers.append(row[0])

  if row[1] not in uniqueNumbers:
    uniqueNumbers.append(row[1])

# Iteration through texts.csv and calls.csv
print("\n\tThere are " + str(len(uniqueNumbers)) + 
      " different telephone numbers in the records.\n")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
