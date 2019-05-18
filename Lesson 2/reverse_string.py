# -*- coding: utf-8 -*-

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

print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")

# -----------------------------------------------------------------------------

# Udacity's Solution

def string_reverser_udacity(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # New empty string for us to build on
    new_string = ""

    # Iterate over old string
    for i in range(len(our_string)):
        # Grab the charecter from the back of the string and add them to 
        # the new string
        new_string += our_string[(len(our_string)-1)-i]

    # Return our solution
    return new_string

# Test Cases

print ("Pass" if ('retaw' == string_reverser_udacity('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser_udacity('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser_udacity('The house code is: 2343')) else "Fail")


