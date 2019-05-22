# -*- coding: utf-8 -*-
# pep8 verified

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

    # time_spent_on_phone for receiver of phone call
    time_spent_on_phone[call[1]] = time_spent_on_phone.get(call[1], 0) + \
        int(call[3])

# The maximum value needs to be calculated only once, hence to improve the
# performance, instead of calculating this inside the for loop, I am
# doing this calculation outside the loop.
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
