class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

head = Node(33)
head.next = Node(8)
head.next.next = Node(23)
head.next.next.next = Node(24)
head.next.next.next.next = Node(34)

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
