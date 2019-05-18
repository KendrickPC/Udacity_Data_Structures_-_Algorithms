# -*- coding: utf-8 -*-

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
  reader = csv.reader(f)
  texts = list(reader)

  for row in texts:
    print("First record of texts, " + (row[0]) + " texts " + (row[1])
    + " at time " + (row[2]))

with open('calls.csv', 'r') as f:
  reader = csv.reader(f)
  calls = list(reader)

  for row in calls:
    print("Last record of calls, " + (row[0]) + " calls " + (row[1])
    + " at time " + (row[2]) + " lasting " + (row[3]) + " seconds")

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number>
at time <time>"
"Last record of calls, <incoming number> calls <answering number>
at time <time>, lasting <during> seconds"
"""

"""
Run Time Analysis:
Worst Case O(n) Efficiency Report:

  Calculation of O(n), for the texts.csv file, is 1. My assumption is that
  n = 1 because there is only one pass through 
  of the for loop with the texts.csv file.

  Calculation of O(n), for the calls.csv file, is 1. My assumption is that 
  n = 1 because there is only one pass through 
  of the for loop with the calls.csv file.

  Therefore, the total of n would be 1 + 1 = 2. My guess is that the
  efficiency of O(n) equals 2 for the texts.csv file and calls.csv file
  combined.

"""


