'''
Task 05: 
Check if left or right child exists.
Define functions has_left_child, has_right_child, so that
they return true if the node has left child, or right
child respectively.
'''

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self):
        return self.value

    def get_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        '''
        if self.left != None:
            return True
        else:
            return False
        '''
        return self.left != None

    def has_right_child(self):
        '''
        if self.right != None:
            return True
        else:
            return False
        '''
        return self.right != None



## check

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")

print("adding left and right children")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")
