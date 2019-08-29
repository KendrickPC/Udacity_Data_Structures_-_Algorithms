# Binary Search Practice Iterative

'''
Let's get some practice doing binary search on an array of integers.
We'll solve the problem two different ways—both iteratively and resursively.

Here is a reminder of how the algorithm works:
	1. Find the center of the list (try setting an upper and lower
	   bound to find the center)
	2. Check to see if the element at the center is your target.
	3. If it is, return the index.
	4. If not, is the target greater or less than that element?
	5. If greater, move the lower bound to just above the current center
	6. If less, move the upper bound to just below the current center
	7. Repeat steps 1-6 until you find the target or until the bounds are
	   the same or cross (the upper bound is less than the lower bound).

Problem statement:
Given a sorted array of integers, and a target value, find the index of
the target value in the array. If the target value is not present in
the array, return -1.

Iterative solution
First, see if you can code an iterative solution (i.e., one that uses loops).
'''

def binary_search(array, target):
	start_index = 0
	end_index = len(array) - 1

	while start_index <= end_index:
		# Integer division in Python3
		mid_index = (start_index + end_index)//2
		mid_element = array[mid_index]

		# If element has been found.
		if target == mid_element:
			return mid_index

		# The target is less than the mid_element.
		elif target < mid_element:
			# Searching only the left half of the array..
			end_index = mid_index - 1
		# The target is greater than the mid_element.
		else:
			# Searching only the right half of the array.
			start_index = mid_element + 1
	
	return -1

def test_function(test_case):
	answer = binary_search(test_case[0], test_case[1])
	if answer == test_case[2]:
		print("Pass!")
	else:
		print("False!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
