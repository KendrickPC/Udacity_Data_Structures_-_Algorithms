'''
Implement a stack using an array:

In this notebook, we'll look at one way to implement a stack.
First, check out the walkthrough for an overview, and then
you'll get some practice implementing it for yourself.

'''

# Create and initialize the stack class:
class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increase array capacity.")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]


    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(3*len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element


# Testing pop() method.
foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack


# _handle_stack_capacity_full test
# foo = Stack()
# # foo.push("Testing!")
# foo.push(0)
# foo.push(1)
# foo.push(2)
# foo.push(3)
# foo.push(4)
# foo.push(5)
# foo.push(6)
# foo.push(7)
# foo.push(8)
# foo.push(9)
# foo.push(10)
# foo.push(11)
# print(foo.arr)

# Add size and is_empty methods test
'''
foo = Stack()
print(foo.size()) # Should return 0
print(foo.is_empty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.is_empty()) # Should return False
'''
#<<< 0
#<<< True
#<<< 1
#<<< False