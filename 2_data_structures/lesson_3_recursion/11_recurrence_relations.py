'''
Problem Statement
Previously, we considered the following problem:

Given a positive integer n, write a function,
print_integers, that uses recursion to print all
numbers from n to 1.

For example, if n is 4, the function should
print 4 3 2 1.

Our solution was:
'''

def print_integers(n):
	# Base Case.
	if n <= 0:
		return
	print(n)
	print_integers(n - 1)

print_integers(5)


# <<< 5
# <<< 4
# <<< 3
# <<< 2
# <<< 1


'''
Note that in Python, the stack is displayed in an "upside down" manner.
This can be seen in the illustration above—the last frame
(i.e. the frame with n = 0) lies at the top of the stack
(but is displayed last here) and the first frame (i.e., the frame with n = 5)
lies at the bottom of the stack (but is displayed first).

But don't let this confuse you. The frame with n = 0 is indeed the top
of the stack, so it will be discarded first. And the frame with n = 5
is indeed at the bottom of the stack, so it will be discarded last.

We define time complexity as a measure of amount of time it takes to run
an algorithm. Similarly, the time complexity of our function print_integers(5),
would indicate the amount of time taken to exceute our function print_integers.
But notice how when we call print_integers() with a particular value of n,
it recursively calls itself multiple times.

In other words, when we call print_integers(n), it does operations
(like checking for base case, printing number) and
then calls print_integers(n - 1).

Therefore, the overall time taken by print_integers(n) to execute would be equal
to the time taken to execute its own simple operations and the time taken to
execute print_integers(n - 1).

Let the time taken to execute the function print_integers(n) be  𝑇(𝑛) .
And let the time taken to exceute the function's own simple operations be
represented by some constant,  𝑘 .

In that case, we can say that

𝑇(𝑛)=𝑇(𝑛−1)+𝑘
 
where  𝑇(𝑛−1)  represents the time taken to execute the function
print_integers(n - 1).

Similarly, we can represent  𝑇(𝑛−1)  as

𝑇(𝑛−1)=𝑇(𝑛−2)+𝑘
 
We can see that a pattern is being formed here:

𝑇(𝑛)=𝑇(𝑛−1)+𝑘 
𝑇(𝑛−1)=𝑇(𝑛−2)+𝑘 
𝑇(𝑛−2)=𝑇(𝑛−3)+𝑘 
𝑇(𝑛−3)=𝑇(𝑛−4)+𝑘  .
.
.
.
.
.
𝑇(2)=𝑇(1)+𝑘 
𝑇(1)=𝑇(0)+𝑘 
𝑇(0)=𝑘1 
Notice that when n = 0 we are only checking the base case and then
returning. This time can be represented by some other constant, 𝑘1 .

If we add the respective left-hand sides and right-hand sides of all
hese equations, we get:

𝑇(𝑛)=𝑛𝑘+𝑘1
 
We know that while calculating time complexity, we tend to ignore
these added constants because for large input sizes on the order of
 105 , these constants become irrelevant.

Thus, we can simplify the above to:

𝑇(𝑛)=𝑛𝑘
 
We can see that the time complexity of our function print_integers(n)
is a linear function of  𝑛 . Hence, we can say that the time complexity
of the function is  𝑂(𝑛) .
'''

