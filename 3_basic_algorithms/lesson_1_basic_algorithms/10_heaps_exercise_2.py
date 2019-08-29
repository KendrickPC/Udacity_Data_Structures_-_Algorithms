# Complete Binary Trees Using Arrays
'''
Although we call them complete binary trees,
and we will always visualize them as binary trees,
we never use binary trees to create them. Instead,
we actually use arrays to create our complete
binary trees.

Let's see how.
[0][1][2][3][4][5][6][7][8]

An array is a contiguous blocks of memory with
individual "blocks" are laid out one after the
other in memory. We are used to visualizing
arrays as sequential blocks of memory.

However, if we visualize them in the following way,
can we find some similarities between arrays and
complete binary trees?

            [0]
          [1] [2]
       [3][4] [5][6]
    [7][8]


Let's think about it.

In a complete binary tree, it is mandatory for all levels before
the last level to be completely filled. If we visualize our array
in this manner, do we satisfy this property of a CBT? All we have
to ensure is that we put elements in array indices sequenially
i.e. the smaller index first and the larger index next. If we do
that, we can be assured that all levels before the last level will
be completely filled.

In a CBT, if the last level is not completely filled, the nodes
must be filled from left to right.
Again, if we put elements in the array indices sequentially,
from smaller index to larger index, we can be assured that if
the last level is not filled, it will certainly be filled from
left to right.

Thus we can use an array to create our Completer Binary Tree.
Although it's an array, we will always visualize it as complete
binary tree when talking about heaps.

Now let's talk about insert and remove operation in a heap.
We will create our heap class which with these two operations.
We also add a few utility methods for our convenience.
Finally, because we know we are going to use arrays to create
our heaps, we will also initialize an array.

Note that we are creating min heaps for now.
The max heap will follow the exact some process.
The only difference arises in the Heap Order Property.

As always we will use Python lists like C-style arrays to make
the implementation as language agnostic as possible.
'''

class Heap:
    def __init__(self, initial_size):
        # Initialize arrays
        self.cbt = [None for _ in range(initial_size)]
        # Denotes next index where new elements should go
        self.next_index = 0

    def insert(self, data):
        pass

    def remove(self):
        pass


# Insert
'''
Insertion operation in a CBT is quite simple. Because we are
using arrays to implement a CBT, we will always insert at the
next_index. Also, after inserting, we will increment the
value of next_index.

However, this isn't enough. We also have to maintain the heap
order property. We know that for min-heaps, the parent node
is supposed to be smaller than both the child nodes.

n = next element should go here
                    
                        10
                    20      40
                  50  30  70  60
                75  n

Counting indices, we know that our next element should go at
index 8. Let's say we want to insert 15 as our next element
in the heap. In that case, we start off by inserting 15 at
index 8.

                        10
                    20      40
                  50  30  70  60
                75  15

Remember, although we are using arrays to implement a CBT,
we will always visualize it as a binary tree. We will only
consider them as arrays while implementing them.

So, we went ahead and insert 15 at index 8. But this violates
our heap order property. We are considering min-heap and the
parent node of 15 is larger.

In such a case, we heapify. We consider the parent node of
the node we inserted and compare their values. In case of
min-heaps, if the parent node is larger than the child node
(the one we just inserted), we swap the nodes.

Now the complete binary tree looks something like

                        10
                    20      40
                  15  30  70  60
                75  50


Is the problem solved?

Swapping the nodes for 15 and 50 certainly solved our problem.
But it also introduced a new problem. Notice 15 and 20. We are
again in the same spot. The parent node is larger than the child
node. And in a min-heap we cannot allow that. So, what do we do?
We heapify. We swap these two nodes just as we swapped our
previous two nodes.

After swapping, our CBT looks like

                        10
                    15      40
                  20  30  70  60
                75  50

Does everything seem fine now?
We only have to consider the nodes that we swapped.
And looks like we are fine.

Now let's take a step back and see what we did.
    - We first inserted our element at the possible index.
    - Then we compared this element with the parent element
      and swapped them after finding that our child node was
      smaller than our parent node. And we did this process
      again. While writing code, we will continue this process
      until we find a parent which is smaller than the child node.
      Because we are traversing the tree upwards while heapifying,
      this particular process is more accurately called up-heapify.

Thus our insert method is actually done in two steps:
    - insert
    - up-heapify
'''

# Time Complexity
'''
Before talking about the implementation of insert,
let's talk about the time complexity of the insert method.                                   

Putting an element at a particular index in an array takes O(1) time.
However, in case of heapify, in the worst case we may have to travel
from the node that we inserted right to the root node
(placed at 0th index in the array). This would take O(h) time.
In other words, this would be an O(log(n)) operation.
Thus the time complexity of insert would be O(log(n)).
'''

# Insert - implementation
'''
Although we are using arrays for our CBT (complete binary tree),
we are visualizing it as a binary tree for understanding the idea.
But when it comes to the implementation, we will have to think
about it as an array. It is an array, after all.

            [0]
           [1][2]
        [3][4][5][6]
     [7][8]  

In the above image, we can safely assume that:
    - index 0 is the root node of the binary tree
    - index 0 is the parent node for indices 1 and 2
      i.e. 1 is the left node of index 0, and 2 is the right node
    - Similarly, 3 and 4 are the child nodes of index 1.
    - And 5 and 6 are the child nodes of index 2

Can we deduce any pattern from this?
    - If you notice carefully, the child nodes
      of 0 are ---> 1 and 2
    - The child nodes of 1 are ---> 3 and 4
    - The child nodes of 2 are ---> 5 and 6

The child nodes of p are ---> 2*(p+1) and 2*(p+2)
i.e. the child nodes of a parent index p are placed at
indices 2*(p+1) and 2*(p+2)

Similarly, can you deduce parent indices from a child index c?
Answer: for a child node at index c, the parent node will
be located at (p-1)//2

*** Note the integer division

Using these ideas, implement the insert method.
'''
class Heap:
    def __init__(self, initial_size):
        # Initialize array
        self.cbt = [None for _ in range(initial_size)]
        # Denoting next index placing new element
        self.next_index = 0

    # Up-heapify before insertion.
    def _up_heapify(self):
        # Setting child_index to next_index
        child_index = self.next_index

        while child_index >= 1:
            # Deducing parent indices from child index
            # logic from above notes.
            parent_index = (child_index-1) // 2
            # Setting parent and child elements to the
            # index of the complete binary tree
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break


    def insert(self, data):
        # Inserting element into the next index.
        self.cbt[self.next_index] = data
        # Heapify function self call.
        self._up_heapify()
        # Increase index by 1
        self.next_index += 1
        # Double the array and copy elements if next_index
        # goes out of array bounds.
        if self.next_index >= len(self.cbt):
            # Setting up temporary CBT
            temp = self.cbt
            self.cbt = [None for _ in range(2*len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]


# Remove
'''
For min-heaps, we remove the smallest element from our heaps.
For max-heaps, we remove the largest element from the heap.

By now, you must have realized that in case of min-heaps,
the minimum element is stored at the root node of the
complete binary tree. Again, we are emphasizing the fact
that we will always visualize a complete binary tree as
a binary tree and not an array.

                   10
            20          40
        15     30     70  60
      75  50


Consider this CBT. Our remove operation should remove 10 from
the tree. But if we remove 10, we need to put the next smaller
element at the root node. But that will again leave one node
empty. So, we will again have to go to our next smaller
element and place it at the node that is empty. This sounds
tedious.

Rather, we use a very simple yet efficient trick to remove
the element. We swap the first node of the tree (which is
the minimum element for a min-heap) with the last node of
the tree.

If we think about the implementation of our complete binary
tree, we know that 10 will now be present at the last index
of the array. So, removing 10 is a O(1) operation.

However, you might have noticed that our complete binary tree
does not follow the heap order property which means that it's
no longer a heap. So, just like last time, we heapify.
This time however, we start at the top and heapify in downward
direction. Therefore, this is also called as down-heapify.

We look at 50 which is present at the root node, and compare
it with both it's children. We take the minimum of the three
nodes i.e. 50, 15, and 40, and place this minimum at the root
node. At the same time, we place 50 at the node which we
placed at the root node.

Following this operation, our CBT looks like:

                15
            50      40
          20  30   70 60
        75
        
Even now the CBT does not follow the heap order property.
So, we again compare 50 with it's child nodes and swap 50
with the minimum of the three nodes.

                15
            20      40
          50  30   70 60
        75

At this point we stop because our CBT follows the heap
order property.
'''

class Heap(object):
    def __init__(self, initial_size=10):
        # Initialize arrays
        self.cbt = [None for _ in range[initial_size]]
        # Denotes next index where new element should go
        self.next_index = 0

    def _down_heapify(self):
        parent_index = 0
        # _down_heapify while loop
        # parent index mathematical logic.
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]
            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)
            # compare with right child
            if right_child is not None:
                min_element = min(parent, right_child)
            # check if parent is properly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def size(self):
        return self.next_index

    def remove(self):
        # Remove and return element at the top of the heap.
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # Place last element of cbt at the root.
        self.cbt[0] = last_element

        # we do not remove the element, rather we allow next
        # `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()

        return to_remove


# Final Heap
'''
Using the insert and remove functions, let's run the heap.
'''

class Heap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def size(self):
        return self.next_index 

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


heap_size = 5
heap = Heap(heap_size)

elements = [1, 2, 3, 4, 1, 2]
for element in elements:
    heap.insert(element)
print('Inserted elements: {}'.format(elements))
    
print('size of heap: {}'.format(heap.size()))

for _ in range(4):
    print('Call remove: {}'.format(heap.remove()))

print('Call get_minimum: {}'.format(heap.get_minimum()))

for _ in range(2):
    print('Call remove: {}'.format(heap.remove()))

print('size of heap: {}'.format(heap.size()))
print('Call remove: {}'.format(heap.remove()))
print('Call is_empty: {}'.format(heap.is_empty()))


# That's it for heaps! Now it's time for the
# next topic, self-balancing trees.