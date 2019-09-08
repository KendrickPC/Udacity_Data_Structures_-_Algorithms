# Search in a Rotated Sorted Array
'''
You are given a sorted array which is rotated at some random
pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your
algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with
'''


def array_search(start, end, input_list, number):
    middle = (start + end) // 2
    # Base case
    if start > end:
        return -1
    # If middle is greater than target number.
    elif input_list[middle] > number:
        if input_list[start] > input_list[end]:
            if input_list[end] < number:
                return array_search(start, middle-1, input_list, number)
            elif input_list[end] > number:
                return array_search(middle+1, end, input_list, number)
            else:
                return end
        else:
            return array_search(start, middle-1, input_list, number)
    # If middle is less than target number.
    elif input_list[middle] < number:
        if input_list[start] > input_list[end]:
            if input_list[end] < number:
                return array_search(start, middle-1, input_list, number)
            elif input_list[end] > number:
                return array_search(middle+1, end, input_list, number)
            else:
                return end
        else:
            return array_search(middle+1, end, input_list, number)

    else: 
        return middle



def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0 
    end = len(input_list) - 1

    if len(input_list) == 0:
        return "\nThe list is empty\n"

    print("(target for search, index of target):")
    return number, array_search(start, end, input_list, number)


print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
# <<< (6, 5)
print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22))
# <<< (10, 9)
print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0], 0)) 
# <<< (0, -1)


# Edge Cases:
print("\nDealing with Duplicates:")
print(rotated_array_search([8, 8, 8, 8, 8, 8, 8], 8))

# Empty list
print(rotated_array_search([], 0))
# <<< The list is empty

# Resources for Reference of Rotated Array Search:
    # https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# Psuedocode
    #https://stackoverflow.com/questions/4773807/searching-in-a-sorted-and-rotated-array




