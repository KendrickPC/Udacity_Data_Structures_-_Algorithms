# Problem 3

### Rearrange Array Elements (without using a sort library)

I begin solving this problem with a divide and conquer technique.
The theory behind this algorithm is to split the input_list array
into a left half and a right half.

The specified requirements for this algorithm require me to not use
a sort function and must have a time complexity of O(nlog(n)).

I start by using a template of the merge sort algorithm.
The main difference between the merge sort algorithm and my 
algorithm is the handling of result comparisons retreived from 
recursion for the first recursive run.

During my first recursive run, I run a comparison. 
My results are then saved to an alternative lists.

The logic for the existence of my alternative list is because my
data is sorted in this alternative list. For this alternative list,
I start from index[0] and alternate values to each list - this
increases each digit position. A combination, satisfying a maximum
sum of two numbers, gives a maximum digit of difference between the
two data points.

#### Time Complexity
With the foundation of my algorithm being based on merge sorting,
the time complexity is O(nlog(n)). An operation of O(1) is added
to my algorithm, which is basically just 1. 

#### Space Complexity

Python automatically dumps previous auxiliary steps of created
arrays; the space complexity is basically O(n). The arrays are 
the length of our input_list.
