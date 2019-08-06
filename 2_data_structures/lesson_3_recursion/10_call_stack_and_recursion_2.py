'''
Another Example:

Here's another example. Let's say we have a function add() which adds
two integers and then prints a custom message for us using the
custom_print() function.
'''


def add(num_one, num_two):
    output = num_one + num_two
    custom_print(output, num_one, num_two)
    return output

def custom_print(output, num_one, num_two):
    print("The sum of {} and {} is: {}".format(num_one, num_two, output))


result = add(8, 5)

'''
What happens "behind-the-scenes" when add() is called,
as in result = add(5, 7)?

Feel free to play with this on the Python tutorial website.
Here are a few points which might help aid the understanding.

We know that when add function is called using result = add(8, 5),
a frame is created in the memory for the add() function.
This frame is then pushed onto the call stack.

Next, the two numbers are added and their result is stored in the
variable output.
On the next line we have a new function call:

custom_print(output, num_one, num_two)

It's obvious that a new frame should be created for this function
call as well. You must have realized that this new frame is now
pushed into the call stack.

We also know that the function which is at the top of the call stack
is the one which Python executes. So, our 
custom_print(output, num_one, num_two) will now be executed.

Python executes this function and as soon as it is finished with
execution, the frame for custom_print(output, num_one, num_two) is
discarded. If you recall, this is the LIFO behavior that we have
discussed while studying stacks.
Now, again the frame for add() function is at the top.
Python resumes operation just after the line where it had left and
returns the output.
'''

