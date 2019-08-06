'''
Call stacks and recursion:

What is a call stack?:

When we use functions in our code, the computer makes use of a
data structure called a call stack. As the name suggests, a call
stack is a type of stack—meaning that it is a Last-In,
First-Out (LIFO) data structure.

So it's a type of stack—but a stack of what, exactly?

Essentially, a call stack is a stack of frames that are used for
the functions that we are calling. When we call a function, say
print_integers(5), a frame is created in memory. All the variables
local to the function are created in this memory frame. And as soon
as this frame is created, it's pushed onto the call stack.

The frame that lies at the top of the call stack is executed first.
And as soon as the function finishes executing, this frame is discarded
from the call stack.

An example:

Let's consider the following function, which simply takes two integers
and returns their sum.
'''


def add(num_one, num_two):
    output = num_one + num_two
    return output


result = add(5, 7)
print(result)


'''
Before understanding what happens when a function is executed, it is
important to remind ourselves that whenever an expression such as
product = 5 * 7 is evaluated, the right hand side of the = sign is
evaluted first. When the right-hand side is completely evaluated, the
result is stored in the variable name mentioned in the left-hand side.

When Python executes line 1 in the previous cell (result = add(5, 7)),
the following things happen in memory:

A frame is created for the add function. This frame is then pushed onto
the call stack. We do not have to worry about this because Python takes
care of this for us.
Next, the parameters num_one and num_two get the values 5 and 7,
respectively. If we run this code in Python tutor website
(http://pythontutor.com/), we can get a nice visualization of what's
happening "behind the scenes" in memory:
'''


'''
Python then moves on to the first line of the function.
The first line of the function is:

output = num_one + num_two

Here an expression is being evaluated and the result is stored in a new
variable. The expression here is sum of two numbers the result of which
is stored in the variable output. We know that whenever an expression is
evaluated, the right-hand side of the = sign is evaluated first.
So, the numbers 5 and 7 will be added first.

Once the right-hand side is completely evaluated, then the assignment
operation happens i.e. now the result of 5 + 7 will be stored in the
variable output.
'''

'''
In the next line, we are returning this value.

  return output

Python acknowledged this return statement.

Now the last line of the function has been executed. Therefore, this
function can now be discarded from the stack frame. Also, the right-hand
side of the expression result = add(5, 7) has finished evaluation.
Now, the result of this evaluation will be stored in the variable result.
'''

'''
Now the next question is how does this behave like a stack?
The answer is pretty simple. We know that a stack is a
Last-In First-Out (LIFO) structure, meaning the latest element
inserted in the stack is the first to be removed.

You can play more with such "behind-the-scenes" of code execution on
the Python tutor website: http://pythontutor.com/
'''

