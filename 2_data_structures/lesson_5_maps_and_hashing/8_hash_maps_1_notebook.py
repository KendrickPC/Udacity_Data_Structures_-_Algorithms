'''
Data structures help us in representing and efficiently manipulating the data associated with these problems.

Let us see if we can use any of the data structures that
we already know to solve the following problem:

Problem Statement:

In a class of students, store heights for each student.

The problem in itself is very simple. We have the data of heights
of each student. We want to store it so that next time someone
asks for height of a student, we can easily return the value.
But how can we store these heights?

Obviously we can use a database and store these values.
But, let's say we don't want to do that for now. We want to use a
data structure to store these values as part of our program.
For the sake of simplicity, our problem is limited to storing
heights of students. But you can certainly imagine scenarios where
you have to store such key-value pairs and later on when someone
gives you a key, you can efficiently return the corrresponding
value.

The class diagram for HashMaps would look something like this.
'''

class HashMap:

    def __init__(self):
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def size(self):
        return self.num_entries


'''
Arrays:

Can we use arrays to store key-value pairs?

We can certainly use one array to store the names of the students
and use another array to store their corresponding heights at the
corresponding indices.

What will be the time complexity in this scenario?

To obtain height of a student, say Potter, Harry, we will have to
traverse the entire array and check if the value at a particular
index matches Potter, Harry. Once we find the index in which this
value is stored, we can use this index to obtain the height from
the second array.

Thus, because of this traveral, complexity for get() operation
becomes  𝑂(𝑛). Even if we maintain a sorted array, the operation
will not take less than  𝑂(𝑙𝑜𝑔(𝑛)) complexity.

What happens if a student leaves a class? We will have to delete
the entry corresponding to the student from both the arrays.

This would require another traversal to find the index. And then
we will have to shift our entire array to fill this gap. Again,
the time complexity of operation becomes 𝑂(𝑛).


Linked List:

Is it possible to use linked lists for this problem?

We can certainly modify our LinkedListNode to have two different 
value attributes - one for name of the student and the other for
height.

But we again face the same problem. In the worst case, we will
have to traverse the entire linked list to find the height of a
particular student. 
Once again, the cost of operation becomes 𝑂(𝑛).


Stacks and Queues:

Stacks and Queues are LIFO and FIFO data structures respectively.
Can you think why they too do not make a good choice for storing
key-value pairs?

Can we do better? Can you think of any data structure that
allows for fast get() operation?

Let us circle back to arrays.

When we obtain the element present at a particular index using
something like arr[3], the operation takes
constant i.e. O(1) time.

For review - Does this constant time operation require
further explanation?

If we think about array indices as keys and the element present
at those indices as values, we can fairly conclude that at least
for non-zero integer keys, we can use arrays.

However, like our current problem statement, we may not always
have integer keys.

If only we had a function that could give us arrays indices
for any key value that we gave it!
'''
