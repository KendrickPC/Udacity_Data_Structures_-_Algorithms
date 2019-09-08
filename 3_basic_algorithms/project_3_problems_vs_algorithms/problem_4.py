# Dutch National Flag Problem
'''
Given an input array consisting on only 0, 1, and 2, sort the array
in a single traversal. You're not allowed to use any sorting function
that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n)
solution but it will not count as single traversal.

Here is some boilerplate code and test cases to start with:
'''

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    middle = 0
    # Set to length of input_list
    high = len(input_list) - 1

    # Condition of while loop is that the middle must be less than or equal
    # to the high variable.
    while middle <= high:
        if input_list[middle] == 0:
            input_list[low], input_list[middle] = input_list[middle], input_list[low]
            # Add one to low variable
            low += 1
            # Add one to middle variable
            middle += 1
        
        elif input_list[middle] == 1:
            # Add one to middle variable
            middle += 1

        else:
            # Swap [middle, high= with [high, middle]
            input_list[middle], input_list[high] = input_list[high], input_list[middle]
            # Subtract one from high variable
            high -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


print("\nNormal Test Cases:")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print("\nEdge Case Testing:")
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])

