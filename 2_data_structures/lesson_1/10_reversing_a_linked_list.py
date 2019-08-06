'''
Reversing a linked list exercise:

Given a singly linked list, return another linked
list that is the reverse of the first.
'''

#Begin helper code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])
#End helper code.

#Efficiency O(n)
def reverse(linked_list):
    new_list = LinkedList()
    node = linked_list.head
    prev_node = None

    #Take node from original linked list and prepend
    #to the new linked list.
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
    new_list.head = prev_node
    return new_list

#Reversing a linked list test.
llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")