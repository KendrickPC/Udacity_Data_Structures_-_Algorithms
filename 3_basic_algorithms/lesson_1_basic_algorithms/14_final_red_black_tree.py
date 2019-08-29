class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s' % (self.value, print_color)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling.
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def __iter__(self):
        yield from self.root.__iter__()

    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        self.rebalance(new_node)

    # Recursive insert function
    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else: 
                current.right = Node(new_val, current, 'red')
                return current.right
        else:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    # Rebalancing Function:
    def rebalance(self, node):
        # Case 1
        if node.parent == None:
            return
        # Case 2
        if node.parent.color == 'black':
            return
        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))

        gp = grandparent(node)
        # Small changes, if there is no grandparent, 
        # cases 4 and 5 will not apply.
        if gp == None:
            return

        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right

        # Case 5
        p = node.parent
        gp = p.parent
        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'


    def rotate_left(self, node):
        # Save off parent of the sub-tree we're rotating.
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now
        # be a left child.
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child.
        node_moving_up.left = node
        node.parent = node_moving_up

        # Connecting to sub-tree's parent.
        # 'node' may have been the root.
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        # After 'node' moves up, the left child will now
        # be a right child
        node.left = node_moving_up.right
        
        # 'node' moves down, to being a right child.
        node_moving_up.right = node
        node.parent = node_moving_up

        # Connecting the sub-tree's parent.
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        node_moving_up.parent = p



# Print tree test function.
def print_tree(node, level=0):
    print('   ' * (level - 1 ) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)



# Test case 1 and 2
tree = RedBlackTree(9)
tree.insert(6)
tree.insert(19)

print_tree(tree.root)
# <<< 9R
# <<< +--6R
# <<< +--19R


# Inserting 13 should flip 6 and 19 to black, as it hits our
# case 3 logic.
print("----" * 10)
tree.insert(13)
print_tree(tree.root)
 
# <<< 9R
# <<< +--6B
# <<< +--19B
# <<<    +--13R


'''
Observe that 13 was inserted as red, and then because Case 3,
6, and 19 flipped to black. 9 was also assigned red, but that
was not a net ch)ange. Because we're not enforcing the 
optional "root is always black" rule, this is acceptable.

Now we're causing some rotations. When inserting 16, it will
go under 13, but 13 does not have a red sibling. 16 rotates
into 13's spot, because it's currently an inside sub-tree.
Then 16 rotates into 19's spot. After these rotations, the
ordering of the Binary Search Tree (BST) has been preserved
and our tree is balanced.
'''

print("----" * 10)
tree.insert(16)
print_tree(tree.root)

# <<< 9R
# <<< +--6B
# <<< +--16B
# <<<    +--13R
# <<<    +--19R




