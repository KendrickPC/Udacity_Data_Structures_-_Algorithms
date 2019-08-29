# Problem 1 Least Recently Used Cache

### __init__
To initialize the variable class, I used an ordered dictionary. 
https://docs.python.org/2/library/collections.html
	
	8.3.5
	Ordered dictionaries are just like regular dictionaries but they
	remember the order that items were inserted. When iterating over
	an ordered dictionary, the items are returned in the order their
	keys were first added.

### get function
Retrieve item from provided key. Return -1 if nonexistent.
	
	For the get function, my objective is to remove the key
	first and insert the key value pair into my dictionary. 
	I need to reverse the insertion order as FIFO - returning the value.
	For my pop() method, I remove and return an element from the
	right side of the deque.
	If no elements are present, I will raise an IndexError. 
	My except KeyError returns -1 if key is nonexistent

### set function
Set the value if the key is not present in the cache.
If the cache is at capacity, remove the oldest item.

	My set function objective is to insert new key value pairs into
	my dictionary.
	If the capacity is equal to the length of the dictionary, I will remove the recently used in FIFO (first in, first out) order.
	My logic for setting (last = false) is explained below: 

	https://docs.python.org/2/library/collections.html
	
	OrderedDict.popitem(last=True)
	The popitem() method for ordered dictionaries returns and removes
	a (key, value) pair. The pairs are returned in LIFO order if last
	is true or FIFO order if false.

### Time complexity
	O(1)