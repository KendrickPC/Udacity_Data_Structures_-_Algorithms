# Problem 4

### Dutch National Flag Problem
I begin solving this problem with setting the low and middle variables to
zero. The high variable is set to the length of the input list.

Since the objective is to create a sort through a single traversal, I set
a while loop condition - the middle must be equal to or less my high variable. 

First, I set the length of input_list.

The condition of my while loop is that the middle must be less than or
equal to the high variable. If this is the case, I add one to the low and
middle variable.
If the input_list[middle] is equal to 1, I add 1 to the middle variable.
The last condition in my while loop is to swap [middle, high] with
[high, middle] and subtract 1 from the high variable. 


### Time Complexity
The time complexity for my algorithm is O(n). 'n' represents the size 
of my input_list and my algorithm provides a single traversal.

### Space Complexity
The space complexity is O(1). No added arrays are used and the sorting 
of our input_list is done in place.
