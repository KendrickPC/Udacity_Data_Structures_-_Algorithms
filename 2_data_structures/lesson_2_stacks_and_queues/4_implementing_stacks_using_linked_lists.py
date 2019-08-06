'''
Implement a stack using a linked list:

Previously, we looked at how to implement a stack using an array.
While that approach does work, we saw that it raises some concerns
with time complexity. For example, if we exceed the capacity of the
array, we have to go through the laborious process of creating a new
array and moving over all the elements from the old array.

What if we instead implement the stack using a linked list?
Can this improve our time complexity? Let's give it a try.

Define a Node class:

Since we'll be implementing a linked list for this, we know that
we'll need a Node class like we used earlier in this lesson.

See if you can remember how to do this, and implement it below.

Note: If you've forgotten, that's completely OK—simply take a look
at the solution in order to remind yourself. Then hide the solution,
take a short break, and see if you can remember how to do it.
Throughout this course, you will find yourself building on concepts
you learned earlier. Whenever this is the case, it's good to take
this same approach (try to remember, then check the solution, then
hide the solution and try to remember again).
This effort will help the ideas stick better.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


'''
Create the Stack class and its __init__ method
In the cell below, see if you can write the __init__ method for our
Stack class. It will need two attributes:

A head attribute to keep track of the first node in the linked list
A num_elements attribute to keep track of how many items are in the stack
'''

class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        # Push node to head of stack.
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1

        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")

'''
Time complexity of stacks using linked lists:

Notice that if we pop or push an element with this stack,
there's no traversal. We simply add or remove the item from
the head of the linked list, and update the head reference.
So with our linked list implementaion, pop and push have a
time complexity of O(1).

Also notice that using a linked list avoids the issue we ran
into when we implemented our stack using an array. In that case,
adding an item to the stack was fine—until we ran out of space.
Then we would have to create an entirely new (larger) array and
copy over all of the references from the old array.

That happened because, with an array, we had to specify some initial
size (in other words, we had to set aside a contiguous block of memory
in advance). But with a linked list, the nodes do not need to be contiguous.
They can be scattered in different locations of memory, an that works just
fine. This means that with a linked list, we can simply append as many
nodes as we like. Using that as the underlying data structure for our stack
means that we never run out of capacity, so pushing and popping items will
always have a time complexity of O(1).
'''
