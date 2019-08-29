# Heap Implementation:
'''
Although heaps are represented as trees, they are
often stored as arrays. 

Since we know how many children each parent has,
(2), and thus know how many nodes will be at 
each level, we can use math where the next node
will fall in the array and then traverse the 
tree.


*Note: Not every array can be represented
as a heap. In general, the numbers need to be
sorted that will sense on a heap.

Think about tree vs. arrays. Since the arrays 
saves us pointers (to other objects), the arrays
saves us space.

'''