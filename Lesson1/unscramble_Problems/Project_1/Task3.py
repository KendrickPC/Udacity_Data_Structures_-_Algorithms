# -*- coding: utf-8 -*-
# PEP8 verified.

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order
with no duplicates.
"""

# Global scope numbers_array to store search results.
# Codes and prefixes for "called by people in Bangalore."
received_codes_and_prefixes = []


def Bangalore_codes():
    # For loop through calls data.
    for call in calls:
        # startswith() method
        # https://www.w3schools.com/python/ref_string_startswith.asp
        if (call[0].startswith("(080)")):
            # store "Received call" phone numbers, from Bangalore line,
            # in received_call_phone_numbers.
            received_call_phone_numbers = call[1]
            # Split recieved_call_phone_numbers into 5 and 5.
            split_phone_numbers = received_call_phone_numbers.split(" ")
            # Get first character of split_phone_numbers
            mobile_prefixes = split_phone_numbers[0][0]
            if mobile_prefixes == "7" or mobile_prefixes == "8" \
                                  or mobile_prefixes == "9":
                # Store first four numbers of phone numbers beginning
                # with 7, 8, or 9
                received_call_phone_numbers = split_phone_numbers[0][0:4]
                # print(received_call_phone_numbers)
            else:
                # Returns 4s and 6s
                position = received_call_phone_numbers.index(")")
                # print(position)
                # Returns e.g. 080, 022, etc... with e.g. (04344) without ()
                received_call_phone_numbers = \
                    received_call_phone_numbers[1:position]
                # print(received_call_phone_numbers)
            if received_call_phone_numbers not in received_codes_and_prefixes:
                received_codes_and_prefixes.append(received_call_phone_numbers)

    # Sort received_codes_and_prefixes array into lexicongraphic order
    lexicographic_order_sort = sorted(received_codes_and_prefixes)
    # print(len(lexicographic_order_sort))

    print("\nThe numbers called by people in Bangalore have codes:")
    for codes_and_mobile_prefixes in lexicographic_order_sort:
        print(codes_and_mobile_prefixes)

Bangalore_codes()

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def percentage_fixed_line_calls_from_Bangalore():

    Bangalore_caller = 0
    Bangalore_on_both_ends = 0

    for call in calls:
        if call[0].startswith("(080)"):
            Bangalore_caller += 1

        if call[0].startswith("(080)") and call[1].startswith("(080)"):
            Bangalore_on_both_ends += 1

    percentage = ((Bangalore_on_both_ends)/(Bangalore_caller)*100)
    # print(percentage)
    # Rounding percentage to two decimal places.
    # https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python
    rounded_percentage = str(round(percentage, 2))
    print("\n" + rounded_percentage + " percent of calls from fixed lines in"
          "Bangalore are calls to other fixed lines in Bangalore.")

percentage_fixed_line_calls_from_Bangalore()

# print(rounded_percentage + "%")
