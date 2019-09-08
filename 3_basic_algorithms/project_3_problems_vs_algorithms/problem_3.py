# PEP8 Verified
# Rearrange Array Elements (without using a sort library)
'''
Rearrange Array Elements so as to form two number such that
their sum is maximum. Return these two numbers. You can assume
that all array elements are in the range [0, 9]. The number of
digits in both the numbers cannot differ by more than 1. You're
not allowed to use any sorting function that Python provides
and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer
can be [542, 31]. In scenarios such as these when there are
more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
'''


def rearrange_digits(input_list: list, first_sort: bool=False):
    """
    Rearrange Array Elements so as to form two number such that
    their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) <= 1:  # Taking care of edge case with nothing in index.
        return input_list

    middle = len(input_list) // 2  # Cutting input_list in half
    left = input_list[:middle]  # Returning left half of list
    right = input_list[middle:]  # Returning right side of list

    left = rearrange_digits(left)  # Recursive call for left half of list
    right = rearrange_digits(right)  # Recursive call for right half of list

    return merge(left, right, first_sort)  # Calling merge function below


def merge(left: list, right: list, first_sort: bool=False):
    merged = []  # Creating an empty array
    left_index = 0  # Setting the left index to 0
    right_index = 0  # Setting the right index to 0

    # Special case for the last merging step.
    if first_sort:
        num_max_left = ''
        num_max_right = ''
        num_to_left = True

        # Divide and Conquer technique beginnning with left index
        while left_index < len(left) and right_index < len(right):
            # If left index is greater than right index
            if left[left_index] > right[right_index]:
                # If number to the left
                if num_to_left:
                    # Setting maximum left number
                    num_max_left = str(right[right_index]) + num_max_left
                else:
                    # Setting maximum right number
                    num_max_right = str(right[right_index]) + num_max_right
                right_index += 1
            
            else:
                # Setting maximum left number
                if num_to_left:
                    num_max_left = str(left[left_index]) + num_max_left
                # Setting maximum right number
                else:
                    num_max_right = str(left[left_index]) + num_max_right
                left_index += 1

            # Distributing numbers to each list (left and right)
            num_to_left = not num_to_left

        # Divide and Conquer technique emptying the remaining indexes
        while left_index < len(left):
            # Emptying left index
            if num_to_left:
                # Setting maximum left number
                num_max_left = str(left[left_index]) + num_max_left
            else:
                # Setting maximum right number
                num_max_right = str(left[left_index]) + num_max_right

            left_index += 1
            num_to_left = not num_to_left

        # Emptying right index
        while right_index < len(right):
            if num_to_left:
                # Setting maximum number on right index (left side)
                num_max_left = str(right[right_index]) + num_max_left
            else:
                # Setting maximum numbert on right index (right side)
                num_max_right = str(right[right_index]) + num_max_right

            right_index += 1
            num_to_left = not num_to_left

        # Returning results of two numbers - one for left side and one for right side
        return [int(num_max_left), int(num_max_right)]

    else:
        # Handling normal merging cases.
        while left_index < len(left) and right_index < len(right):

            if left[left_index] > right[right_index]:
                # Appending right index to merge array
                merged.append(right[right_index])
                right_index += 1
            else:
                # Appending left index to merged array
                merged.append(left[left_index])
                left_index += 1

        # Adding left indeces to merged array
        merged += left[left_index:]
        # Adding right indeces to merged array
        merged += right[right_index:]

        # Returning answer, with two values, in the merged array.
        return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


print("\nNormal Test Cases:")
print("\nTest #1:")
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [531, 42] == result else "Fail")

print('\nTest #2:')
list_num = [2, 4, 6, 8, 3, 5]
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [642, 853] == result else "Fail")

print('\nTest #3:')
list_num = [11, 12, 13, 14]
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [1311, 1412] == result else "Fail")

# Edge Case Testing:
print("\nEdge Case Testing:")
print("\nTest #4:")
list_num = [0, 0, 0, 0, 0]
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [0, 0] == result else "Fail")

print("\nTest #5:")
list_num = [8]
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [8] == result else "Fail")

print("\nTest #6:")
list_num = []
result = rearrange_digits(input_list=list_num, first_sort=True)
print(result)
print("Pass" if [] == result else "Fail")
