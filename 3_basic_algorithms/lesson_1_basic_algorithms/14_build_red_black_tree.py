# Build a Red-Black Tree
'''
In this notebook, we'll walk through how you might build a
red-black tree. Remember, we need to follow the red-black
tree rules, on top of the binary search tree rules.
Our new rules are:
    - All nodes have a color
    - All nodes have two children (use NULL nodes)
        - All NULL nodes are colored black
    - If a node is red, its children must be black
    - The root node must be black (optional)
        - We'll go ahead and implement without this for now
    - Every path to its descendant NULL nodes must contain
      the same number of black nodes.
'''

# Sketch
'''
Similar to our binary search tree implementation, we will
define a class for nodes and a class for the tree itself.
The Node class will need a couple new attributes. It is no
longer enough to only know the children, because we need to
ask questions during insertion like, "what color is
my parent's sibling?". So we will add a parent link as
well as the color.
'''

class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

'''
For the tree, we can start with a mostly empty implementation.
However, we know we want to always insert nodes with the color
red, so let's fill in the constructor to insert the root node.
'''

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        pass

    def search(self, find_val):
        return False

# Insertion
'''
Now how would we design our insert implementation?
We know from our experience with BSTs how most of it will work.
We can re-use that portion and augment it to assign colors
and parents.
'''

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, current, new_val)
            else:
                current.right = Node(new_val, current, 'red')
        else:
            if current.left:
                self.insert_helper(current.left, current, new_val)
            else:
                current.left = Node(new_val, current, 'red')

# Rotations
'''
At this point, we are only making a BST, with extra attributes.
To make this a red-black tree, we need to add the extra sauce
that makes red-black trees awesome. We will sketch out some
more code for rebalancing the tree based on the case, and 
fill them in one at a time.

First, we need to change our insert_helper to return the node
that was inserted so we can interrogate it when rebalancing.
'''

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_value:
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


    def rebalance(self, node):
        pass


# Case 1
'''
We have just inserted the root node.
If we're enforcing that the root node must be black, we can 
change its color. We are not enforcing this, so we are all
done. Four to go.
'''

def rebalance(node):
    if node.parent == None:
        return

# Case 2
'''
We inserted under a black parent node.

This this through, we can observe the following: we inserted
a red node beneath a black node. The new children (the Null 
nodes) are black by definition, and our red node replaced a
black-Null-node. So the number of black nodes for any paths
from parents is unchanged. Nothing to do in this case, either.
'''

def rebalance(node):
    if node.parent == None:
        return
    if node.parent.color == 'black':
        return

# Case 3
'''
The parent and its sibling of the newly inserted node are both 
red. 

Okay, we're done with free cases. In this specific case, we
can flip the color of the parent and its sibling. We know
they're both red in this case, which means the grandparent is
black. It will also need to flip. At this point we will have a 
freshly painted red node at the grandparent. At that point, we
need to do the same evaluation. If the grandparent turns red,
and its sibling is also red, that's case #3 again. Guess what
that means?  Time for more recursion.

We will define grandparent and pibling (a parent's sibling)
methods later, for now let's focus on the core logic.
'''

def rebalance(node):
    if node.parent == None:
        return
    if node.parent.color == 'black':
        return
    # From here, we know the parent's color is red.
    # Case 3
    if pibling(node).color == 'red':
        pibling(node).color = 'black'
        node.parent.color = 'black'
        grandparent(node).color = 'red'
        self.rebalance(grandparent(node))


# Case #4
'''
The newly inserted node has a red parent, but that parent has
a black sibling.

These last cases get more interesting. The criteria above 
actually govern cases 4 and 5.  What seperates them is if the 
newly inserted node is on the inside or the outside of the sub
tree. We define inside and outside like this:

    inside
        EITHER
            - the new node is a left child of its parent, but
              its parent is a right child, or
            - the new node is a right child of its parent, but
              its parent is a left child.

    outside
        - the opposite of inside, the new node and its parent
          are on the same side of the grandparent.


Case 4 is to handle the inside scenario. In this case, we need
to rotate. As we will see, this will not finish balancing
the tree, but will now qualify for Case 5.

We rotate against the inside-ness  of the new node. If the new
node qualifies  for case 4, it needs to move into its parent's 
spot.If it's on the right of the parent, that's a rotate 
left. If it's on the left of the parent, that's a rotate right.
'''

def rebalance(self, node):
    # Cases 1-3 are omitted for this example.
    # Case #4
    gp = grandparent(node)
    if gp.left and node == gp.left.right:
        self.rotate_left(parent(node))
    elif gp.right and node == gp.right.left:
        self.rotate_right(parent(node))
    # TODO: Case 5

'''
To implement rotate_left and rotate_right, think about what we 
want to accomplish. We want to take one of the node's children 
and have it take the place of its parent. The given node
will move down to a child of the newly parental node.
'''

def rotate_left(self, node):
    # Save-off the parent of the sub-tree we're rotating.
    p = node.parent

    node_moving_up = node.right
    # After 'node' moves up, the right child will now be
    # a left child.
    node.right = node_moving_up.left
    # 'node' moves down, to being a left child.
    node_moving_up.left = node
    node.parent = node_moving_up

    # Now we need to connect to the sub-tree's parent
    # 'node' may have been the root.
    if p != None:
        if node == p.left:
            p.left = node_moving_up
        else:
            p.right = node_moving_up
    node_moving_up.parent = p


def rotate_right(self, node):
    # Save off the parent of the sub-tree we're rotating.
    p = node.parent

    node_moving_up = node.left
    # After 'node' moves up, the left child will now be a
    # right child
    node.left = node_moving_up.right
    # 'node' moves down, to be a right child.
    node_moving_up.right = node
    node.parent = node_moving_up

    # Now we need to connect the sub-tree's parent
    # 'node' may have been the root.
    if p != None:
        if node == p.left:
            p.left = node_moving_up
        else:
            p.right = node_moving_up
    node_moving_up.parent = p


# Case 5
'''
Now that case 4 is resolved, or if we didn't qualify for case
4, and have an outside sub-tree already, we need to rotate
again. If our new node is a left child of a left child, we
rotate right. If our new node is a right of a right child, we
rotate left. This is done on the grandparent node.

But after this rotation, our colors will be off. Remember that
for cases 3, 4, and 5, the parent of the new node is red. But
we will have rotated a red node with a red child up, which
violates our rule of all red nodes having two black children.
So after rotating, we switch the colors of the (original)
parent and grandparent nodes. 
'''

def rebalance(self, node):
    # cases 1-3 omitted.
    # Case 4
    gp = grandparent(node)
    if node == gp.left.right:
        self.rotate_left(node.parent)
    elif node == gp.right.left:
        self.rotate_right(node.parent)

    # Case 5
    p = node.parent
    gp = p.parent
    if node == p.left:
        self.rotate_right(gp)
    else:
        self.rotate_left(gp)
    p.color = 'black'
    gp.color 'red'


# Results of combining all our efforts for the following:










