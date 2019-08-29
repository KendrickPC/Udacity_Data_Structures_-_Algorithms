# Priority Queues - Intuition
'''
Consider the following scenario -

A doctor is working in an emergency wing at a hospital.
When patients come in, a nurse checks their symptoms and
based on the severity of the illness, sends them to the
doctor. For e.g. a guy who has had an accident is sent
before someone who has come with a runny nose.
But there is a slight problem.
There is only one nurse and only one doctor.
In the amount of time the nurse takes to check the
symptoms, the doctor has to work alone with the patients,
hurting their overall productivity.

The doctor comes to you for help.
Your job is to write a small software in which patients will
enter their symptoms and will receive a priority number based
on their illness. The doctor has given you a list of common
ailments, and the priority in which he would prefer seeing
them. How would you solve the priority problem?
'''

# Priority Queues:
'''
Like the name suggests, a priority queue is similar to a
regular queue, except that each element in the queue has a
priority associated with it. A regular queue is a FIFO data
structure, meaning that the first element to be added to the
queue is also the first to be removed.

With a priority queue, this order of removal is instead based
on the priority. Depending on how we choose to set up the
priority queue, we either remove the element with the most
priority, or an element of the least priority.

For the sake of discussion, let's focus on removing the element
of least priority for now.
'''

# Functionality:
'''
If we were to create a PriorityQueue class,
what methods would it need to have?

Here are the two key methods:

    insert - insert an element
    remove - remove an element

And we can also add the same utility methods that we
had in our regular Queue class:

    front - returns the element at the front of the queue
    size - returns the number of elements present in the queue
    is_empty - returns True if there are no elements in the queue,
               and False otherwise.

As part of this functionality, we will need a way of assigning
priorities to the items.

A very common way to solve the patient-doctor problem mentioned
above would be to assign each ailment a priority. For e.g.

    * A running nose may be assigned priority 1
    * Fever may be assigned 2
    * Accident may get a priority 10

You will find this theme recurring in all of programming.
We use numbers to effectively represent data.

For the sake of simplicity, let's only consider integers here.
Let us assume a scenario where we get integers as input and we
assign a priority on how large or small they are.
Let us say the smaller the number, the smaller its priority.
So, in our simplified version of the problem statement the
value of the integer serves as a priority.

Our goal is to create a queue where the element with the lowest
priority is removed first. Therefore, the remove method will
remove the smallest number from the priority queue. Thus, the
largest number will be the last to be removed from the priority
queue and the smallest number will be the first to be removed.
'''

# How Should We Implement It?
'''
What we've described above is just the abstract characteristics
that we expect from this data structure. As with stacks and
queues (and other abstract data types), there is more than one
way that we could implement our priority queue such that it
would exhibit the above behaviors.

However, not all implementations are ideal. When we implemented
a regular queue earlier, you may remember the enqueue and dequeue
methods had a time complexity of  𝑂(1) . Similarly, we would like
the insert and remove methods on our priority queue to be fast.

So, what underlying structure should we use to implement the
priority queue such that it will be as efficient as possible?
Let's look at some different structures and consider the pros and cons.
'''

# Arrays
'''
Earlier, we saw that one way to implement a queue was by using an array.
We could do a similar thing for priority queues.
We could use the array to store our data.

Insertion in an array is very fast.
Unless the array is full, we can do it in O(1) time.

*Note: When the array is full, we will simply create a new array
and copy all the elements from our old array to new array.
It's exactly similar to what we do for our queue's
implementation using arrays.

What about removal? We always want to remove the smallest or highest
priority data from the array, depending on if this is a max-heap or min-heap.
In the worst case, we will have to search the entire array,
which will take O(n) time. Thus, to remove the element,
the time complexity would be O(n).

This also creates an additional problem for us.
The index from which we removed the element is now empty.
We cannot leave empty indices in our array.
Over the course of operations, we will be wasting a lot of
space if we did that.

Therefore, insertion no longer happens in O(1) time.
Rather, every time we insert, we will have to look for these empty
indices and put our new element in the first empty index we find.
In the worst case, this also takes O(n) time.
Therefore, our time complexity with arrays
(for both insertion and removal) would be O(n).
'''

#LinkedList
'''
Insertion is very easy in a linked list. If we maintain a variable
to keep track of the tail of the linked list, then we can simply add
a new node at this location. Thus, insertion takes O(1) time.

For removal, we will have to traverse the entire list and find the
smallest element, which will require O(n) time.

Note that with linked lists, unlike arrays, we do not have to worry
about empty indices.

A linked linked certainly seems to be a better option than an array.
Although they have the same time complexity for removal,
the time complexity for insertion is better.
'''

# HashMap
'''
The same problem lies in HashMap as well. We can insert in O(1) time.
Although, we can remove an element from a HashMap in O(1) time, but we
have to first search for the smallest element in the map.
This will again take O(n) time. 
Therefore, the time complexity of remove is O(n) for hashmaps.
'''

#Binary Search Trees
'''
Binary Search Trees are laid out according to the value of the node
that we want to insert. All elements greater than the root go to the
right of the root, and all elements smaller than the root go to the
left of the root.

If we assume that our Binary Search tree is balanced, insertion
would require O(h) time in the worst case. Similarly, removal would
also require O(h) time. Here h is the height of the binary search tree.

                    4
                  2   7
                 1 3 5 8

A Binary Tree is called a Balanced Binary Tree when the difference
between the heights of it's left subtree and right subtree do not
differ by more than one. Additionally, to be balanced, all the
subtrees of the binary tree must also be balanced.

For a balanced tree, we can safely approximate the height of the
tree h to log(n). Thus, both insertion and removal
require O(log(n)) time in a binary search tree.

However, in the worst case, our binary search tree might just be
a sequential list of nodes (stretching to the right or to the left).
Consider the following tree:

        1
         2
          3
           4

In such a scenario the binary search tree effectively turns into a
linked list. In this case, the time complexity would be O(n).

To avoid this situation, we would need a self-balancing tree which
would incure additional complexity.

We could use any of the above data structures to implement our
priority queue — and they would work, in the sense that they would
exhibit the outward behavior we expect in a priority queue.

However, none of them acheived our goal of having 𝑂(1) time
complexity for both insert and remove.
To do that, we will need to explore something new: A heap.
'''

# Heaps
'''
A heap is a data structure with the following two main properties:
    1. Complete Binary Tree
    2. Heap Order Property

1. Complete Binary Tree - Like the name suggests we use a binary
   tree to create heaps. A complete binary tree is a special type
   of binary tree in which all levels must be filled except for
   the last level. Moreover, in the last level, the elements
   must be filled from left to right.

Example A:
            10
          25  15
         6  9
A. is a complete binary tree. Notice how every level except the
last level is filled. 
Also notice how the last level is filled from left to right

Example B:
            10
          25  15
         6   9

B. is not a complete binary tree. Although evey level is filled
except for the last level. Notice how the last level is not
filled from left to right. 25 does not have any right node and
yet there is one more node (9) in the same level towards the
right of it. It is mandatory for a complete binary tree to be
filled from left to right.

Example C:
            10
          25
         6  9

C. is also not a binary tree. Notice how the second level is
not completely filled and yet we have elements in the third level.
The right node of `10` is empty and yet we have nodes in the next level.

    - Heap Order Property - Heaps come in two flavors
        - Min Heap
        - Max Heap

    Min Heap - In the case of min heaps, for each node, the parent
    node must be smaller than both the child nodes. It's okay even
    if one or both of the child nodes do not exists.
    However if they do exist, the value of the parent node must be smaller.
    Also note that it does not matter if the left node is greater than the
    right node or vice versa. The only important condition is that the root
    node must be smaller than both it's child nodes.

    Max Heap - For max heaps, this condition is exactly reversed.
    For each node, the value of the parent node must be larger than
    both the child nodes.
    
    Thus, for a data structure to be called a Heap, it must satisfy
    both of the above properties.
        1. It must be a complete binary tree
        2. It must satisfy the heap order property. 
           If it's a min heap, it must satisfy the heap order
           property for min heaps.
           If it's a max heap, it should satisfy the heap order
           property for max heaps.
'''

# Complete Binary Tree
'''
Let's go back to our complete binary tree A.
    
    * n = next node can only go here.

            10
          25  15
         6 9 (n)

If we have to insert one more node, where should the next node go?
Because A. is a complete binary tree, the next node can only go as
the left node of 15 aka (n).

Similarly, let's look back A. again. If we have to delete a node
from A., which node should we delete? Again, to ensure that our
tree remains a complete binary tree even after deleting a node,
we can only remove 9.

Thus, we know which node to remove and where to insert a new node.
Notice that both of these operations do not depend upon values of
other nodes. Rather, both insert and remove operations on a
complete binary tree depend upon the position of the last
inserted node.

This cell may require some visualization due to
the mathematics involved

Now that we know about a complete binary, let's think about it in
terms of Priority Queues. We talked about binary search trees where
the complexity for insert and remove operation would be O(log(n))
if the BST (binary search tree) is balanced.

In case of a complete binary tree, we do not have to worry about
whether the tree is balanced or not.

    Max number of nodes in 1st level = 1
    Max number of nodes in 2nd level = 2
    Max number of nodes in 3rd level = 4
    Max number of nodes in 4th level = 8

We see that there is a clear patter here.
    Max number of nodes in hth level = 2^(ℎ−1)

Also, we can calculate the max number of nodes from 1st level
to hth level = (2^ℎ)-1

Similarly, we can calculate the min number of nodes from
1st level to hth level = 2^(ℎ−1) 

*** Note: the minimum number of nodes from 1st level
    to hth level = max number of nodes from 1st level
    to (h-1)th level + 1

Thus, in a complete binary tree of height h, we can be assured
that the number of elements n would be between these
two numbers i.e.


Thus, in a complete binary tree of height h, we can be assured
that the number of elements n would be between these two numbers i.e.

    2^(ℎ−1) <= 𝑛 <= (2^ℎ)−1

        If we write the first inequality in base-2 logarithmic
        format we would have the following:

            log[base2](2^(ℎ−1)) <= log[base2]n
                        or
            h <= log[base2] n+1
    
    Similarly, if we write the second equality in base-2
    logarithmic format:
            
            log[base2](𝑛+1) <= log[base2]2^ℎ
                        or
            log[base2](𝑛+1) <= ℎ

Thus the value of our height h is always:
        log[base2](𝑛+1) <= ℎ <= log[base2]n + 1


We can see that the height of our complete binary tree will always
be in the order of O(h) or O(log(n))

So, if instead of using a binary search tree, we use a complete
binary tree, both insert and remove operation will have the
time complexity of log[base2]n
'''

# Heaps for Priority Queues
'''
Let's take a step back and reflect on what we have done.

    1. We have examined popular data structures and observed
       their time complexities.
    2. We have looked at a new data structure called Heap
    3. We know that Heaps have two properties -
            i. CBT (Complete Binary Tree)
            ii. Heap Order Property
    4. We have looked at what CBT is and what Heap Order Property is

By now, it must have been clear to you that we are going to use
Heaps to create our Priority Queues. But are you convinced that
heaps are a good structure to create Priority Queues?

Answer:

1. Other than Binary Search trees, all other popular data
   structures seemed to have a time complexity of O(n) for
   both insertion and removal.

2. Binary Search Trees seemed like an effective data structure
   with average case time complexity of O(log(n) (or O(h)) for
   both the operations.
   However, in the worst case, a Binary Search Tree may not be
   balanced and instead behave like a linked list. In such a case,
   the time complexity in terms of height would still be O(h) but
   because the height of the binary search tree will be equal to
   the number of elements in the tree, the actual time complexity
   in terms of number of elements n would be O(n).

3. The CBT property of Heaps ensures that the tree is always balanced.
   Therefore, the height h of the tree will always be equal to log(n).

4. The Heap Order Property ensures that there is some definite
   structure to our Complete Binary Tree with respect to the value of
   the elements. In case of a min-heap, the minimum element will
   always lie at the root node. Similarly, in case of a max-heap,
   the maximum element will always lie at the root node.
   In both the cases, every time we insert or remove an element,
   the time complexity remains O(log(n)).

Therefore, because of the time complexity being O(log(n)), we
prefer heaps over other popular data structures to create our
Priority Queues.
'''
