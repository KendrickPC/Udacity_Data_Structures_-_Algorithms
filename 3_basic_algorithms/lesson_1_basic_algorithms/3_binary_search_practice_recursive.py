# Binary Search Practice Recursive

# This function only takes two inputs: array and target. 
# It does not require a start_index and/or end_index.
def binary_search_recursive(array, target):
	return binary_search_recursive_solution(array, target, 0, len(array) - 1)


def binary_search_recursive_solution(array, target, start_index, end_index):
	# Base case checking.
	if start_index > end_index:
		# Denoting fail in input.
		return -1

	# Integer division in Python3
	mid_index = (start_index + end_index) // 2
	# Setting mid_element to the middle of the mid_index array.
	mid_element = array[mid_index]

	# split mid_index by half and take the lower end.
	# in this specific test function, a pass is already
	# achieved.
	if mid_element == target:
		return mid_index
	elif target < mid_element:
		# Taking the lesser half of the split.
		return binary_search_recursive_solution(array, target, start_index, mid_index - 1)
	else:
		# Returning upper half of split array. 
		# This will usually run if there are only two
		# elements left.
		return binary_search_recursive_solution(array, target, mid_index + 1, end_index)


def test_function(test_case):
	answer = binary_search_recursive(test_case[0], test_case[1])
	if answer == test_case[2]:
		print("Pass!")
	else:
		print("Fail!")


# Test Case 1
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 14
index = 14
test_case = [array, target, index]
test_function(test_case)
# <<< Fail!

# Test Case 2
target = 3
index = 3
test_case = [array, target, index]
test_function(test_case) 
# <<< Pass!

# Test Case 3
target = -5
index = -5
test_case = [array, target, index]
test_function(test_case)
# <<< Fail!