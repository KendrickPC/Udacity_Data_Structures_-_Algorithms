# Depth First Search Intro

'''
Tree Traversal:

    Traversing a tree: "visiting" all nodes once.
    Used for searching, inserting, and deleting nodes.

    Two Types:
        Depth First Search (DFS)
        Breadth First Search (BFS)

        Depth First Search:
            Pre-order
            In-order
            Post-order

        Breadth First Search:
'''

'''
Traverse a Tree (Depth First Search):

Traversing a tree means "visiting" all the nodes in the tree once.
Unlike an array or linked list, there's more than one way to walk
through a tree, starting from the root node.

Traversing a tree is helpful for printing out all the values stored
in the tree, as well as searching for a value in a tree, inserting
into or deleting values from the tree.
There's depth first search and breadth first search.

Depth first search has 3 types:
    - pre-order,
    - in-order,
    - post-order.

Let's walk through pre-order traversal by hand first, and then try it out in
code.

        apple
    banana cherry
  dates
'''


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # Define __repr__ to decide what a print statement displays
    # for a Node object.
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


def pre_order(tree):

    visit_order = list()
    root = tree.get_root()

    def traverse(node):

        if node:
            # Visit node
            visit_order.append(node.get_value())
            # Traverse left
            traverse(node.get_left_child())
            # Traverse right
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

# <<< ['apple', 'banana', 'dates', 'cherry']
print(pre_order(tree))


# In-Order Traversal:
def in_order(tree):
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):    
        if node:
            # Traverse left
            traverse(node.get_left_child())
            # Visit node
            visit_order.append(node.get_value())
            # Traverse right
            traverse(node.get_right_child())

    traverse(root)
    return visit_order

# <<< ['dates', 'banana', 'apple', 'cherry']
print(in_order(tree))


# Post-Order Traversal:
def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # Traverse left
            traverse(node.get_left_child())
            # Traverse right
            traverse(node.get_right_child())
            # visit order
            visit_order.append(node.get_value())

    traverse(root)
    return visit_order

# <<< ['dates', 'banana', 'cherry', 'apple']
print(post_order(tree))
