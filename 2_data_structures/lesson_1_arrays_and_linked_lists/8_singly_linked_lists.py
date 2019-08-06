'''
Singly Linked Lists

In this linked list, each node in the list is connected only to
the next node in the list.

[2] -> [1] -> [4] -> [3] -> [5]

This connection is typically implemented by setting the next
attribute on a node object itself.
'''

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(1)

print(head.value)
print(head.next.value)
"""

'''
Above we have a simple linked list with two elements, `[2, 1]`.
Usually you'll want to create a `LinkedList` class as a wrapper for
the nodes themselves and to provide common methods that operate on the list.
For example you can implement an `append` method that adds a value to the
end of the list.

Note that if we're only tracking the head of the list, this runs in linear
time O(n) since you have to iterate through the entire list to get to the
tail node. However, prepending (adding to the head of the list) can be done
in constant O(1) time. Let's implement this `prepend` method.
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
     # Write the append function within the class.
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node).
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return 


linked_list = LinkedList()
linked_list.append(33)
linked_list.append(45)
linked_list.append(99)

node = linked_list.head

while node:
    print(node.value)
    node = node.next
