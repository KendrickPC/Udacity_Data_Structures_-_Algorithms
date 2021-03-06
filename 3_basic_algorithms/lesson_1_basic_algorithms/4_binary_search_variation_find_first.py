# Binary Search Variation
'''
Variations on Binary Search:
Now that you've gone through the work of building a binary search
function, let's take some time to try out a few exercises that are
variations (or extensions) of binary search.
We'll provide the function for you to start:
'''

def recursive_binary_search(target, source ,left=0):
    # Base case handling.
    if len(source) == 0:
        return None
    # Integer division in Python3
    center = (len(source)-1) // 2

    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)

'''
Find First

The binary search function is guaranteed to return an index for
the element you're looking for in an array, but what if the
element appears more than once????

* What if the element appears more than once? *

Consider this array:

[1, 3, 5, 7, 7, 7, 8, 11, 12]

i.e. Let's find the number 7:
'''

'''
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
print(recursive_binary_search(7, multiple))
# <<< 4 
# This returns the second occurance of my target, but not the third 
# and any target occurence thereafter.
'''

'''
Hmm...
Looks like we got the index 4, which is correct, but what if we
wanted to find the first occurrence of an element, rather than
just any occurrence?

Write a new function: find_first() that uses binary_search as
a starting point.

Hint: You shouldn't need to modify binary_search() at all.
'''

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
# <<< 3 
print(find_first(7, multiple))
# <<< None
print(find_first(9, multiple))
