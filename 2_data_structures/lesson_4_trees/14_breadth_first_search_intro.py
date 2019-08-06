'''
Breadth First Search:
    Visits the tree one level at a time.
    BFS in graph structure (shortest path).


Traverse a Tree (breadth first search):

You'll see breadth first search again when we learn about
graph data structures, so BFS is very useful to know.


'''


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


    def set_value(self, value):
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
        return self.left is not None

    def has_right_child():
        return self.right is not None

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

'''
        Tree Structure

            apple
       banana  cherry
    dates

Breadth First Search:

Breadth first traversal of the tree would visit
the nodes in this order:

# <<< ['apple', 'banana', 'cherry', 'dates']

Think Through the Algorithm:
We are walking down the tree one level at a time. So we start with
apple at the root, and next are banana and cherry, and next
is dates.

1) start at the root node
2) visit the root node's left child (banana), then right child
(cherry)
3) visit the left and right children of (banana) and (cherry).
'''


'''
Queue:

Notice that we're waiting until we visit "cherry" before visiting "dates".
It's like they're waiting in line. We can use a queue to keep track
of the order.
'''
from collections import deque
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)

print(q.deq())
print(q)
'''
def breadth_first_search(node):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            # visit root and append it to list
            visit_order.append(node)
            visit_order.append(node(get_right_child()))
            # visit_order.append(node.get_value())

    traverse(root)
    return visit_order



print(breadth_first_search(tree))
'''

# dequeue the next node in the queue. 
# "visit" that node
# also add its children to the queue

node = q.deq()
visit_order.append(node)
if node.has_left_child():
    q.enq(node.get_left_child())
if node.has_right_child():
    q.enq(node.get_right_child())
    
print(f"visit order: {visit_order}")
print(q)

