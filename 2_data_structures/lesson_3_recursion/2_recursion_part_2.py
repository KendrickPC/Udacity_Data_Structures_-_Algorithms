
'''
Slicing:

Let's look at recursion on arrays and how you can run into the problem of slicing
the array. If you haven't heard the term slicing, it's the operation of taking a
subset of some data. For example, the list a can be sliced using the following
operation: a[start:stop]. This will return a new list from index start (inclusive)
to index stop (exclusive).

Let's look at an example of a recursive function that takes the sum of all numbers
in an array. For example, the array of [5, 2, 9, 11] 
would sum to 27 (5 + 2 + 9 + 11).
'''


def sum_array(array):
	# Base case.
	if len(array) == 1:
		return array[0]

	return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr)) 


'''
Looking at this, you might think it has a running time of O(𝑛), but that isn't
correct due to the slice operation array[1:]. This operation will
take O(𝑘) time to run where  𝑘  is the number of elements to copy. 
So, this function is actually O(𝑘∗𝑛) running time complexity and O(𝑘∗𝑛)
space complexity.

To visualize this, let's plot the time it takes to slice.
'''

"""
import matplotlib.pyplot as plt
import statistics
import time
#import matplotlib inline

n_steps = 10
step_size = 1000000
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
times = []

# Calculate the time it takes for the slice function to run with different sizes of k
for array_size in array_sizes:
    start_time = time.time()
    big_array[:array_size]
    times.append(time.time() - start_time)

# Graph the results
plt.scatter(x=array_sizes, y=times)
plt.ylim(top=max(times), bottom=min(times))
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()
"""

'''
As you can see, it's linear time to slice.

Instead of slicing, we can pass the index for the element that we want to use
for addition. That will give us the following function:
'''


def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))


'''
That eliminates the need to do slicing. With the two different functions
implemented, let's compare the running times.
'''

def sum_array_iter(array):
    result = 0
    
    for x in array:
        result += x
    
    return result

arr = [1, 2, 3, 4]
print(sum_array_iter(arr))


import matplotlib.pyplot as plt
import statistics
import time

n_steps = 10
step_size = 200
array_sizes = list(range(step_size, n_steps*step_size, step_size))
big_array = list(range(n_steps*step_size))
sum_array_times = []
sum_array_index_times = []

for array_size in array_sizes:
    subset_array = big_array[:array_size]
    
    start_time = time.time()
    sum_array(subset_array)
    sum_array_times.append(time.time() - start_time)
    
    start_time = time.time()
    sum_array_index(subset_array, 0)
    sum_array_index_times.append(time.time() - start_time)
    
    
plt.scatter(x=array_sizes, y=sum_array_times, label='sum_array')
plt.scatter(x=array_sizes, y=sum_array_index_times, label='sum_array_index')
plt.ylim(
    top=max(sum_array_times + sum_array_index_times),
    bottom=min(sum_array_times + sum_array_index_times))
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.plot()


'''
The sum_array_iter function is a lot more straightforward than the two
recursive functions, which is important. Second, to help ensure an answer
that is correct and bug free, you generally want to pick the solution that
is more readable. In some cases recursion is more readable and in some cases
iteration is more readable. As you gain experience reading other
people’s code, you’ll get an intuition for code readability.
'''
