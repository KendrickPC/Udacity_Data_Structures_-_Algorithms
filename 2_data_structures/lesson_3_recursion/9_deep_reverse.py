'''
Problem Statement:

Define a procedure, deep_reverse, that takes as input a list,
and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list, and if any
of those elements are lists themselves, reverses all the elements
in the inner list, all the way down.

Note: The procedure must not change the input list itself.
'''


def is_list(element):
    return isinstance(element, list)

def deep_reverse(arr):
    return deep_reverse_func(arr, 0)

def deep_reverse_func(arr, index):
    # Base case
    if index == len(arr):
        return list()

    output = deep_reverse_func(arr, index + 1)

    # If the element is in the list, deep reverse the list.
    if is_list(arr[index]):
        to_append = deep_reverse(arr[index])
    else:
        to_append = arr[index]

    output.append(to_append)
    return output

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
