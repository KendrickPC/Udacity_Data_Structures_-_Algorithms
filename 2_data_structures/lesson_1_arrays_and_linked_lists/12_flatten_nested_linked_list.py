'''
Flatten a Nested Linked List:

Suppose you have a linked list where the value of each node is a sorted
linked list (i.e., it is a nested list). Your task is to flatten this
nested list—that is, to combine all nested lists into a single
(sorted) linked list.

First, we'll need some code for generating nodes and a linked list:
'''


# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged



class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next


'''
Computational Complexity:

Lets start with the computational complexity of merge. 
Merge takes in two lists. Let's say the lengths of the lists
are 𝑁sub1  and  𝑁sub2. Because we assume the inputs are sorted,
merge is very efficient.

It looks at the first element of each list and adds the smaller
one to the returned list. Every time through the loop we are
appending one element to the list, so it will take  𝑁sub1+𝑁sub2  
iterations until we have the whole list.

The complexity of flatten is a little more complicated to calculate.
Suppose our NestedLinkedList has  𝑁  linked lists and each list's
length is represented by  𝑀sub1,𝑀sub2,...,𝑀sub𝑁 .

We can represent this recursion as:

𝑚𝑒𝑟𝑔𝑒(𝑀1,𝑚𝑒𝑟𝑔𝑒(𝑀2,𝑚𝑒𝑟𝑔𝑒(...,𝑚𝑒𝑟𝑔𝑒(𝑀𝑁−1,𝑚𝑒𝑟𝑔𝑒(𝑀𝑁,𝑁𝑜𝑛𝑒)))))

Let's start from the inside. The inner most merge returns the  𝑛𝑡ℎ  
linked list. The next merge does  𝑀𝑁−1+𝑀𝑁  comparisons. The next
merge does  𝑀𝑁−2+𝑀𝑁−1+𝑀𝑁  comparisons.

Eventually we will do  𝑁  comparisons on all of the  𝑀𝑁  elements.
We will do  𝑁−1  comparisons on  𝑀𝑁−1  elements.
'''



'''
This can be generalized as:

n
∑ 𝑛 ∗ 𝑀𝑛
N
'''