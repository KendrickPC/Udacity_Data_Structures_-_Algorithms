'''
Recursion:

Recursion is a technique for solving problems where the solution to a
particular problem depends on the solution to a smaller instance
f the same problem. 

Consider the problem of calculating 2^5. Let's assume to calculate this,
you need to do one multiplication after another. That's 2 * 2 * 2 * 2 * 2.
We know that 2^5 = 2 * 2^4. If we know the value of 2^4,
we can easily calculate 2^5.

We can use recursion to solve this problem, since the solution to the
original problem (2^n) depends on the solution to a smaller
instance (2^{n-1}) of the same problem.
The recursive solution is to calculate 2*2^{n-1} for all n that is
greater than 0. If n is 0, return 1. We'll ignore all negative numbers.

Let's look at what the recursive steps would be for calculating 2^5.

2^5 = 2 * 2^4

2^5 = 2 * 2 * 2^3

2^5 = 2 * 2 * 2 * 2^2

2^5 = 2 * 2 * 2 * 2 * 2^1

2^5 = 2 * 2 * 2 * 2 * 2 * 2^0

2^5 = 2 * 2 * 2 * 2 * 2 * 1

Code:

Let's look at the recursive function `power_of_2`, which calculates 2^n.
'''

def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)

print(power_of_2(5))


'''
As you can see, the function calls itself to calculate the smaller instance
of the solution. Let's break down the power_of_2 function, starting with
the first two lines.

if n == 0:
    return 1

These lines contain the base case. This is where you catch edge cases that
don't fit the problem ( 2∗2𝑛−1 ). Since we aren't considering any  𝑛<0  valid,
2∗2𝑛−1  can't be used when  𝑛  is  0 . This section of the code returns the
solution to  20  without using  2∗2𝑛−1 .

return 2 * power_of_2(n - 1)

This code is where it breaks the problem down into smaller instances.
Using the formula  2𝑛=2∗2𝑛−1 , the power_of_2 function calls itself to
calculate  2𝑛−1 . To better understand what is happening, let's look at
the call stack with an example.
'''

'''
Call Stack:

Let's follow the call stack when calling power_of_2(5):

First power_of_2(5) is called.

Then power_of_2(5) calls power_of_2(4)
Then power_of_2(4) calls power_of_2(3)
Then power_of_2(3) calls power_of_2(2)
Then power_of_2(2) calls power_of_2(1)
Then power_of_2(1) calls power_of_2(0)

At this point, the call stack will look something like this:

  File "<ipython-input-27-9e8459c7465f>", line 5, in power_of_2
    return 2 * power_of_2(n - 1)
  File "<ipython-input-27-9e8459c7465f>", line 5, in power_of_2
    return 2 * power_of_2(n - 1)
  File "<ipython-input-27-9e8459c7465f>", line 5, in power_of_2
    return 2 * power_of_2(n - 1)
  File "<ipython-input-27-9e8459c7465f>", line 5, in power_of_2
    return 2 * power_of_2(n - 1)
  File "<ipython-input-27-9e8459c7465f>", line 3, in power_of_2
    return 1

Let's look at a cleaner view of the stack:

    -> power_of_2(5)
        -> power_of_2(4)
            -> power_of_2(3)
                -> power_of_2(2)
                    -> power_of_2(1)
                        -> power_of_2(0)

Each function is waiting on the function it called to complete.
So, power_of_2(5) is waiting for power_of_2(4), power_of_2(4)
is waiting for power_of_2(3), etc..

The function power_of_2(0) will return  1 
Using the 1 returned from power_of_2(0), power_of_2(1)
will return  2∗1 
Using the 2 returned from power_of_2(1), power_of_2(2)
will return  2∗2 

Using the 16 returned from power_of_2(4), power_of_2(5)
will return  2∗16 

Finally, the result of  25  is returned!  25=2∗24=2∗16=32
'''

'''
Practice Problem:

Implement sum_integers(n) to calculate the sum of all
integers from  1  to  𝑛  using recursion.
For example, sum_integers(3) should return  6  ( 1+2+3 ).
'''

def sum_of_integers(n):
	if n == 1:
		return 1
	return n + sum_of_integers(n - 1)

print(sum_of_integers(3))


'''
Gotchas:

When using recursion, there are a few things to look out for that
you don't have to worry about when running a loop (iteratively).
Let's go over a few of those items.

Call Stack:

We went over an example of the call stack when calling
power_of_2(5) above. In this section, we'll cover the limitations
of recursion on a call stack. Run the cell below to create a really
large stack. It should raise the 
error RecursionError: maximum recursion depth exceeded in comparison.
'''

# print(power_of_2(10000))
#<<< RecursionError: maximum recursion depth exceeded in comparison

'''
Python has a limit on the depth of recursion to prevent a stack overflow.
https://en.wikipedia.org/wiki/Stack_overflow

However, some compilers will turn tail-recursive functions
https://en.wikipedia.org/wiki/Recursion_(computer_science)#Tail-recursive_functions
into an iterative loop to prevent recursion from using up the stack.
Since Python's compiler doesn't do this, you'll have to watch out
for this limit.
'''
