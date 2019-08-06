class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(99)
head.next = Node(33)
head.next.next = Node(55)


def print_linked_list(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

print_linked_list(head)