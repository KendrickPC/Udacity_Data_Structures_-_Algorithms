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

"""
Run Time Analysis:
Worst Case O(n) Efficiency Report:

  Calculation of O(n), for the uniqueNumbers = [] array is 1 because there 
  will be 1 call through the array to check if a "new number" is unique 
  in the list. 

  Calculation of O(n), for the texts.csv file, is 2. My assumption is that
  n = 2 because there is one(1) pass through for the uniqueNumbers array, 
  one pass through with the for loop for row[0], and one pass through  
  for row[1] on the texts.csv file.

  Calculation of O(n), for the calls.csv file, is 2. My assumption is that
  n = 2 because there is  one pass through for the row[0] array and 
  one pass through with the row[1] array on the calls.csv file.

  Therefore, the total of n would be 1 + 2 + 2 = 5. My guess is that O(n) equals 5
  for the texts.csv file and calls.csv file combined.
"""