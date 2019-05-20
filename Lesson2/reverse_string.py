# -*- coding: utf-8 -*-
# PEP8 Verified

"""
In this first exercise, the goal is to write a function that takes a string
as input and then returns the reversed string.
For example, if the input is the string "water", then the output
should be "retaw".
While you're working on the function and trying to figure out how to
manipulate the string, it may help to use the print statement so
you can see the effects of whatever you're trying.
"""

# https://www.w3schools.com/python/python_howto_reverse_string.asp
# There is no built-in function to reverse a String in Python.
# The fastest (and easiest?) way is to use a slice that steps backwards,
# -1.

"""
    Reverse the input string
    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
"""


def string_reverser(our_string):
    our_string = our_string[::-1]
    print(our_string)

string_reverser("water")
string_reverser("This simple code works perfectly.")
