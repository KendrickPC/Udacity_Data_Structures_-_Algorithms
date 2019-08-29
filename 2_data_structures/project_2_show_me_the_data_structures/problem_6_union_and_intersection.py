# PEP8 Verified.
# Union and Intersection of Two Linked Lists
'''
Your task for this problem is to fill out the union and
intersection functions. The union of two sets A and B is
the set of elements which are in A, in B, or in both A and B.

The intersection of two sets A and B, denoted by A ∩ B, is the
set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that
is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test
cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + "->"
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Creating union dictionary and linked list.
    union_dictionary = dict()
    union_list = LinkedList()
    # Setting node to head of first input.
    node = llist_1.head
    # Running a while loop here get add +1 to node value.
    while node:
        if union_dictionary.get(node.value):
            union_dictionary[node.value] = union_dictionary.get(node.value) + 1
        else:
            union_dictionary[node.value] = 1

        # Setting current node to next node.
        node = node.next

    # Working on second input into union function.
    node = llist_2.head
    # Running while loop to obtain the same objective for
    # first input into union function.
    while node:
        if union_dictionary.get(node.value):
            union_dictionary[node.value] = union_dictionary.get(node.value) + 1
        else:
            union_dictionary[node.value] = 1

        # Setting current node to next node.
        node = node.next

    # Appending value of union_dictionary to union_list
    for i in union_dictionary:
        union_list.append(i)

    return union_list


def intersection(llist_1, llist_2):
    # Creating intersection dictionary and linked list.
    intersection_dictionary = dict()
    intersection_list = LinkedList()
    # Creating a temporary dictionary to store list.
    temporary_dictionary = dict()
    # Setting node to the head of first input in intersection function.
    node = llist_1.head
    # Running a while loop to store values into temporary
    # dictionary. Then connect to next node.
    while node:
        temporary_dictionary[node.value] = 1
        # Setting current node to next node.
        node = node.next

    # Working on second input into intersection function.
    node = llist_2.head
    while node:
        if temporary_dictionary.get(node.value):
            intersection_dictionary[node.value] = 1
        # Setting current node to next node.
        node = node.next

    # Appending value of intersection_dictionary into 
    # intersection list.
    for i in intersection_dictionary:
        intersection_list.append(i)

    return intersection_list


def union_and_intersection(element_1, element_2):

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Union:")
    print(union(linked_list_1, linked_list_2))

    print("Intersection:")
    print(intersection(linked_list_1, linked_list_2))


# First Test Case
print("\nFirst test case:")
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
union_and_intersection(element_1, element_2)

# Second Test Case
print("\nSecond test case:")
element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]
union_and_intersection(element_1, element_2)

# Third Test Case
print("\nThird test case:")
element_1 = []
element_2 = []
union_and_intersection(element_1, element_2)

# Fourth Test Case
print("\nFourth test case:")
element_1 = [1, 2, 3]
element_2 = [97, 98, 99]
union_and_intersection(element_1, element_2)



