# Efficiency of Binary Search
'''
Time Complexity of Binary Search
How do we calculate the time complexity for binary search?

We can approximate the efficiency of binary search by answering
this question: How many steps do we have to take in the
worst-case scenario?

At each step, we check the middle element—and then we can rule
out about half of the numbers (discarding everything to either
the left or right). So if we start with nn numbers, then after
the first step we will have half that many, or (n/2) left that
we still need to check.

Note: It won't always be exactly half the numbers that get
discarded. If you have an even number of elements, you will
have to check either the lower or higher of the middle two
elements — and this means you'll rule out either half of the
array, (n/2) or one more than half the array, (n/2) + 1.

But when we calculate time complexity using big O notation,
we tend to ignore such small details, because they have
negligible impact on the efficiency.
Usually, we are concerned with large input sizes — on the
order of, say, 10^5.

Imagine an array of size 10^5!
It doesn’t really matter if each step rules out exactly half
of the array, (10^5 / 2) or slightly more than half of the array,
(10^5 / 2) + 1
So to keep things simple here, we will ignore the +1.
'''

# ***NOTE*** The efficiency of a binary search algorithm
# is O(log(n)) with log base as 2.


# QUESTION 1 OF 5
'''
The total number of integers in the array is n.

After each step, we reduce the number of elements
remaining that we need to search.

How many elements will we have left after each step?

AFTER THIS MANY STEPS...   THIS MANY ELEMENTS LEFT TO SEARCH...
		0							n
		1							n/2
		2							n/4
		3							n/8
		4							n/16
'''

'''
Here's what we're doing at each step:

In the first step, we discard half of the numbers — that is,
(n/2) numbers. So, the total number of remaining integers
is also half, or (n/2).

In the second step, we discard half of the numbers that were
left with us from the first step. We had (n/2) integers, so we
discard half of these numbers and hence are left with
(n/4) integers.

Similarly, in the next step we again discard half of the
numbers that were left in the last step. Thus, we are now
left with (n/8) integers.

We'll continue this process until, in the final step, we will
have only one integer left.
We will compare with this integer and check whether this is
our target.
'''

# QUESTION 2 OF 5
'''
You probably saw from the above exercise that there is a pattern
to the sequence. Which of these correctly describes the pattern?

(Remember, each expression represents the number of elements left
to search after we've completed one step.)

Answer: n, (n/2), (n/4), (n/8), (n/16), (n/32), (n/64) ... 2, 1

We start with n, which is the total number of indexes to search
for our target number. And then, each time we check an index,
we cut the search space in half.

Notice that this is the same as repeatedly multiplying by (1/2)
'''


# QUESTION 3 OF 5
'''
Let's try a concrete example. Suppose we have n = 8, meaning that
we have an array with eight elements. And suppose that the target
number is not even in the array, so we must proceed with the
maximum number of steps (i.e., the worst-case scenario).

In that case, what will we get after each step?

STEPS 				Remaining Elements to Search
Before any steps 		 		8
After first step 			8*(1/2) = 4
After second step 			4*(1/2) = 2
After third step 			2*(1/2) = 1
'''


# QUESTION 4 OF 5
'''
Instead of showing each step like this:
8*(1/2) = 4
4*(1/2) = 2
2*(1/2) = 1

We could simply write:
8*(1/2)*(1/2)*(1/2) = 1

Which can be re-written in exponential notation as...

Answer:  8 * (1/2)^3 = 1
'''

'''
Thus, with a starting array size of n = 8, it will take at most
three steps to find the target number.

So that's a specific example, but let's see if we can come up
with a general equation that models this.
'''

# QUESTION 5 OF 5
'''
Our equation above was 8 * (1/2)^3 = 1
Let's see if we can turn that into a general equation.

Which of these equations correctly models the relationship
between the number of steps and the input size?

(Where s is the number of steps and n is the array size.)

Answer: n * (1/2)^s
'''

'''
Now, what we need to know for calculating efficiency is the
number of steps, s. We can solve for that algebraically.

In case you want to follow the math, here are the steps:
n * (1/2)^s = 1

Use the properties of negative exponents to rearrange the fraction:
n * 2^-s = 1

Divide both sides by 2^-s 
(n * 2^-s) / (2^-s) = 1 / (2^-s)
n = 1 / (2^-s)

Again use the properties of negative exponents to rearrange
the fraction:
n = 2^s

Take the logarithm (base 2) of both side:
log[base2](n) = log[base2](2^s)
log[base2](n) = s


The bottom line? The number of steps is equal to the logarithm
of the input size:
s = log[base2](n)

This is the number of steps it will require to find the target
number in the worst case scenario.
In big-O notation, we would say that the time complexity
is O(log[base2](n))

If we look back at our comparison of computational complexities,
we can see that this is extremely efficient:


***NOTE*** See efficiency_binary_search.png file.


In fact, this efficiency is the second best on the graph, with only constant time complexity, O(1) performing better!

Even as the input size grows very large, the number of steps
required is still surprisingly small.

Going back to our guess-the-number game, you should now see
why it's possible — using binary search — to correctly guess
a number, out of 100. with only a handful of tries.
If you like, go back and try inputs of 200 or even 1000.
The algorithm will still perform quite well!
(For an input of 1000, you might need slightly more than 7 tries.)
'''
