'''
Build a Node:

* Define a node, what are the three things you'd expect in a node?
* Define class called `Node`, and define a constructor that takes
  no arguments, and sets the three instance variables to `None.
* Note: coding from a blank cell (or blank piece of paper) is
  good practice for interviews!
'''

# Define a node
class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")


