class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Moving to the tail of the Node.
        node = self.head
        while node.next:
             node = node.next

        node.next = Node(value)
        return

list_with_loop =LinkedList([33, 23, 8, 99, 34])

# Creating a loop where the last node points back to the second node.

loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

def isCircular(linked_list):
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
    
    pass


# Testing
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ("Pass" if isCircular(list_with_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([-4, 7, 2, 5, -11])) else "Fail")
print ("Pass" if not isCircular(LinkedList([1])) else "Fail")
print ( "Pass" if isCircular(small_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([])) else "Fail")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Moving to the tail of the Node.
        node = self.head
        while node.next:
             node = node.next

        node.next = Node(value)
        return

list_with_loop =LinkedList([33, 23, 8, 99, 34])

# Creating a loop where the last node points back to the second node.

loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

def isCircular(linked_list):
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
    
    pass


# Testing
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ("Pass" if isCircular(list_with_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([-4, 7, 2, 5, -11])) else "Fail")
print ("Pass" if not isCircular(LinkedList([1])) else "Fail")
print ( "Pass" if isCircular(small_loop) else "Fail")
print ("Pass" if not isCircular(LinkedList([])) else "Fail")
