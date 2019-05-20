# -*- coding: utf-8 -*-
# PEP8 Verified

# Check if a given string is an anagram of another given string
# https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-26.php


def anagram_checker(str1, str2):
    # Returns str1 and str2 with lower case.
    lower_case_string_1 = str1.lower()
    lower_case_string_2 = str2.lower()
    # print(lower_case_string_1)
    # print(lower_case_string_2)

    # Returns a list of letters broken down into an array.
    list_string_1 = list(lower_case_string_1)
    list_string_2 = list(lower_case_string_2)
    # print(list_string_1, list_string_2)

    # Sorts the array, in lower case, in lexicographic order.
    list_string_1.sort()
    list_string_2.sort()

    # If else statement to check length of anagram being compared.
    if len(list_string_1) != len(list_string_2):
        print("Your words have different lengths buddy. Try again.")
    else:
        # Compares the sorted array and returns True or False
        print(list_string_1 == list_string_2)

# Test cases
anagram_checker('race', 'EARC')
anagram_checker('clean', 'air')
anagram_checker('art', 'rat')
anagram_checker('art', 'ratttt')
anagram_checker('free', 'tree')
