# Searching in a Rotate Sorted Array

### Explanation
For this searching in a rotated array problem, I basically use a 
divide and conquer technique. Given a sorted array which is rotated
at some random pivot point, I am given a target value to search.

If the target is found in the array, I return its index. Otherwise,
I return -1.

I'm running the assumption that there are no duplicates in the array
and my algorithm's runtime complexity must be in the order of O(log(n))

For my array search function, I find the middle variable value by adding
the start and end and dividing it by two.

I handle the base case first - if the start is greater than the end, I
return -1.

The first scenario I tackle is having a situation in which the middle
value is greater than the target number. If so, run my array_search
algorithm and return the output.

The second scenario I tackle is having a situation in which the middle
value is less than the target number. The algorithm used to return the
output is pretty much the same, with some minor differences. 

This is basically a binary search algorithm with a divide and conquer
approach.

#### Algorithm Time Complexity
My approach to this problem is based on the binary search algorithm,
which is O(log(n)). With recursion depth, the efficiency is squaring
the depth. But isolating the number of iterations, we runtime becomes
log(n), basically O(log(n))

#### Algorithm Space Complexity
The space complexity of this algorithm is an in place search. It is
independent of the input_list, therefore making it O(1).
