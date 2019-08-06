# Stacks and Queues

	Stacks are really useful when you only care about the most
	recent elements added into the list.

	"Push"and "Pop" are associated with stacks.

	L.I.F.O (Last in, first out) data structure

##### 3_Implementing Stacks into an Array
	
	With a stack, we can only access elements at one end. 
	It's very much like a container of Pringles chips.

	Functionality:
	Our goal will be to implement a Stack class that has the following behaviors:

	push - adds an item to the top of the stack
	pop - removes an item from the top of the stack (and returns the value of that item)
	size - returns the size of the stack
	top - returns the value of the item at the top of stack (without removing that item)
	is_empty - returns True if the stack is empty and False otherwise

##### 4_Implementing_stacks_using_a_linked_list
	
	Review Notes 3 - 9

##### 10_Queues:
	
	First In, First Out data structure.

	First element (oldest) in queue is head.
	Last element (newest) in queue is tail.

	Adding element from tail is called Enqueue.
	Deleting element head is called Dequeue.

	Deques (pronounced "Deck") go both ways. 
	Priority Queue. Assign elements priority.


	Functionality:
	Once implemented, our queue will need to have the following functionality:

	enqueue - adds data to the back of the queue
	dequeue - removes data from the front of the queue
	front - returns the element at the front of the queue
	size - returns the number of elements present in the queue
	is_empty - returns True if there are no elements in the queue, and False otherwise
	_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
	Also, if the queue is empty, dequeue and front operations should return None.


