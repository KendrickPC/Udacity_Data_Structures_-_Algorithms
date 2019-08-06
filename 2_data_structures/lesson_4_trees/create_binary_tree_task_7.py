'''
Task 07: 
Setting Root Node in Constructor

Let's modify the Tree constructor so that it takes an input that
initializes the root node. Choose between one of two options:
1) the constructor takes a Node object
2) the constructor takes a value, then creates a new Node object
   using that value.
'''

# 1. 
class Tree(object):
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root


# 2.
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root



# Which method do I think is better?
'''
I would choose method #2 because I wouldn not assume the user knows how 
to write a new Node class; the user can just store the value they want to use.
'''
