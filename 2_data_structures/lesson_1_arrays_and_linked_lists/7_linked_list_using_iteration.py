'''
Creating a linked list using iteration

Previously, we created a linked list using a very manual
and tedious method. We called next multiple times on our head node.

Now that we know about iterating over or traversing the linked list,
is there a way we can use that to create a linked list?

We've provided our solution below—but it might be a good exercise
to see what you can come up with first. Here's the goal:

See if you can write the code for the create_linked_list function below
The function should take a Python list of values as input and return the
head of a linked list that has those values
There's some test code, and also a solution, below — give it a try for
yourself first, but don't hesitate to look over the solution if you get stuck
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)


def create_linked_list(input_list):
    head = None
    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(value)
    return head


### Test Code
input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)
