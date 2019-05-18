# -*- coding: utf-8 -*-

# Read file into texts and calls.
import csv

# How do I sort a list of dictionaries by a value of the dictionary?
# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of
# -dictionaries-by-a-value-of-the-dictionary/73050#73050
from operator import itemgetter

# Global scope variable of dictionary for storage.
time_spent_on_phone = {}

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

for call in calls:
    # time_spent_on_phone for caller
    time_spent_on_phone[call[0]] = time_spent_on_phone.get(call[0], 0) + \
                                   int(call[3])
    # time_spent_on_phone for reciever of phone call
    time_spent_on_phone[call[1]] = time_spent_on_phone.get(call[1], 0) + \
                                   int(call[3])
    sum_of_time_on_phone_in_seconds = max(time_spent_on_phone.items(),
                                          key=itemgetter(1))

# print(sum_of_time_on_phone_in_seconds)
# ('(080)33251027', 90456)

print("\n{} spent the longest time, {} seconds, on the phone during "
      "September 2016.".format(*sum_of_time_on_phone_in_seconds))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone
during September 2016.".
"""

"""
Run Time Analysis:
Worst Case O(n) Efficiency Report:

  Calculation of O(n), for the calls.csv file, is 3. My assumption is that
  n = 3 because there is one pass through collecting the outgoing call time,
  one pass through for the receiving call time, and one pass through for my
  time_spent_on_phone dictionary with the sum_of_time_on_phone_in_seconds
  sorting.
"""

# pep8 verified

#Task 2

# accessing all the elements of calls.csv we have to access each element in list - time complexity : O(n)
# add duration for both sender and reciever as time spending will be same for both update the record in dictonary of (telephonenumber and duration)

# sorted the dictonary based on duration of call will take O(nlogn)

# and accessing the first element in constant time

# Total time complexity : O(n+nlogn+1) which is equvivalent to O(nlogn(n)) in worst case
