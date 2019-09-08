# Max and Min in a Unsorted Array

'''
In this problem, we will look for smallest and largest integer from a
list of unsorted integers. The code should run in O(n) time.
Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a
single traversal?
'''

import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # Base Case for empty list
    if len(ints) == 0:
        return None

    # Representing Infinite
    # https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python?rq=1
    maximum_value = -float('inf')
    mininum_value = float('inf')

    # Running for loop for ints list.
    for i in ints:
        # Integer search for maximum value
        if i > maximum_value:
            maximum_value = i
        # Integer search for minimum value
        if i < mininum_value:
            mininum_value = i

    return (mininum_value, maximum_value)


print("\nNormal Test Cases:")
## Example Test Case of Ten Integers
l = [i for i in range(0, 99)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 98) == get_min_max(l)) else "Fail")

# Test case for two negative numbers.
l = [i for i in range(-15, -1)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((-15, -2) == get_min_max(l)) else "Fail")

# Edge Cases
print("\nEdge Test Cases:")
# Empty list testing
l = []
random.shuffle(l)
print("Pass" if (None == get_min_max(l)) else "Fail")

l = [i for i in range(99, -99)]
random.shuffle(l)
print("Pass" if (None == get_min_max(l)) else "Fail")


'''
Sorting usually requires O(n log n) time Can you come up with
a O(n) algorithm (i.e., linear time)?
'''


