# -*- coding: utf-8 -*-

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
Properties of set()
- No parameters are passed to create the empty set
- Dictionary can also be created using set, but only
keys remain after conversion, values are lost.
https://www.geeksforgeeks.org/python-set-method/
"""


def telemarketer_filtering():
    possible_telemarketers = set()
    phone_numbers_using_texting = set()
    callers = set()
    receivers = set()

    # Adding rows 1 and 2 from texts to  for filtering later.
    for text in texts:
        phone_numbers_using_texting.add(text[0])
        phone_numbers_using_texting.add(text[1])

    # Separating calls.csv into two separate sets of callers and receivers.
    for call in calls:
        callers.add(call[0])
        receivers.add(call[1])

    # Loop through row 1 of calls.csv file 
    for caller in callers:
        # Matching caller phone numbers against phone numbers receiving
        # calls. Checking for duplicates.
        if caller not in receivers:
            # Matching caller phone numbers against phone numbers making
            # texts. Checking for duplicates.
            if caller not in phone_numbers_using_texting:
                possible_telemarketers.add(caller)

    # Lexicographic sort of possible telemarketer phone numbers.
    possible_telemarketers = sorted(possible_telemarketers)

    print("These numbers could be telemarketers: ")
    # Using for loop to print out one per line order.
    for telemarketer in possible_telemarketers:
        print(telemarketer)

telemarketer_filtering()

# print(len(possible_telemarketers))
# 43 unique telephone numbers.

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic
order with no duplicates.
"""
