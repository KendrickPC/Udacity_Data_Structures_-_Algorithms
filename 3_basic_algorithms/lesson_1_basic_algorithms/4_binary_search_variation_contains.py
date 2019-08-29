# Binary Search Variation Contains
'''
Contains
The second variation is a function that returns a boolean value
indicating whether an element is present, but with no information
about the location of that element.

For example:
    letters = ['a', 'c', 'd', 'f', 'g']
    print(contains('a', letters)) ## True
    print(contains('b', letters)) ## False

There are a few different ways to approach this, so try it out,
and we'll share two solutions after.
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


# Option 1: Wrap the binary search
def contains(target, source):
    return recursive_binary_search(target, source) is not None


# Option 2: Build a simpler binary search directly into the function:
# Native implementation of binary search in the `contains` function.
def contains(target, source):
    if len(source) == 0:
        return False
    center = (len(source)-1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center+1:])
    else:
        return contains(target, source[:center])




letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))
# <<< True
print(contains('b', letters))
# <<< False