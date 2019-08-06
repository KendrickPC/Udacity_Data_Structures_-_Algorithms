'''
Task 02: add a constructor that takes the value as a parameter:
Copy what you just made, and modify the constructor so that it
takes in an optional value, which it assigns as the node's value.
Otherwise, it sets the node's value to None.
'''

class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None


## Check
node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node("apple")
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")


# <<< value: None
# <<< left: None
# <<< right: None

# <<< value: apple
# <<< left: None
# <<< right: None
