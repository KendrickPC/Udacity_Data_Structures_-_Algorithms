'''
Implementing and traversing a linked list

In this notebook we'll get some practice implementing a
basic linked list—something like this:  

  2 --> 1 --> 4 --> 3 --> 5 --> None
head

Key Characteristics of Linked Lists:
    - A linked list is made up of nodes.
    - Each node has data/value and index for each element.
'''

# Implementing a simple linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
print(head.value)
#<<< 2
print(head.next)
#<<< None

new_node = Node(33)
head.next = new_node
print(head.next.value)
#<<< 33
print(new_node.value)
#<<< 33


# In practice, I would do the following:
head = Node(8)
head.next = Node(34)
print(head.value)
#<<< 8
print(head.next.value)
#<<< 34


