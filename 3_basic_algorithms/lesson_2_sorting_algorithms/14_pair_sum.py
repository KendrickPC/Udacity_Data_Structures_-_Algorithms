# Pair Sum
'''
Problem Statement
Given an input array and a target value (integer), find two values
in the array whose sum is equal to the target value. 
Solve the problem without using extra space. 
You can assume the array has unique values and will never have
more than one solution.
'''


def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """

    # Sort the list
    arr.sort()
    # Initialize two pointers - one from the start of the array and 
    # the other from the the end.
    front_index = 0
    back_index = len(arr) - 1

    # Shift the pointers
    while front_index < back_index:
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        # Sum < target --> shift front pointer forwards
        elif front + back < target: 
            front_index += 1
        # Sum > target --> Shift back pointer backwards
        else:
            back_index -= 1

    return [None, None]


# Test of pair/sum function.
def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")



input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
