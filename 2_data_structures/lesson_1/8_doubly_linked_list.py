'''
Doubly Linked Lists

This type of list has connections backwards and
forwards through the list.

[2] <--> [1] <--> [4] <--> [3] <--> [5]
'''

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

'''
Now that we have backwards connections it makes
sense to track the tail of the linked list as well
as the head.
'''

'''
Exercise: Implement a doubly linked list that can append
to the tail in constant time O(n). Make sure to include forward
and backward connections when adding a new node to the list.
'''

class DoublyLinkedList:
    # Doubly Linked List __init__ does not need a value.
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return


# Test your class here

linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous


#<<< Going forward through the list, should print 1, -2, 4

#<<< Going backward through the list, should print 4, -2, 1

