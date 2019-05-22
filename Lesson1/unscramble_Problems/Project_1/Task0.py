# -*- coding: utf-8 -*-
# PEP8 verified

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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number>
at time <time>"
"Last record of calls, <incoming number> calls <answering number>
at time <time>, lasting <during> seconds"
"""


def first_record_of_texts():
    # First record of texts.
    text = texts[0]
    # print(text)
    result = "First record of texts, " + text[0] + " texts " + text[1] + \
             " at time " + text[2] + "."
    return result

print(first_record_of_texts())


def last_record_of_calls():
    # Last record of calls.
    call = calls[-1]
    # print(call)
    result = "Last record of calls, " + call[0] + " calls " + call[1] + \
             " at time " + call[2] + ", lasting " + call[3] + " seconds."
    return result

print(last_record_of_calls())
