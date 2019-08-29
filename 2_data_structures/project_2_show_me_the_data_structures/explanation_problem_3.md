### Huffman Encoding: 
My Huffman encoding uses a dictionary to store frequencies of single
characters in my input string. The time and space efficiency of this
is O(n) - all characters are checked and a dictionary insert and
search is done in O(1).

Characters are then sorted by frequency; using my import Priority
Queue library, making the min/max element on top of the queue.
My priority_queue.get() sorts internally. My put() operation is 
O(n log n).

My Huffman Tree is built from the codes_received function starting
at the root. My codes_received function is recursive, storing 
character prefixes in the priority_queue dictionary by traversing
the Huffman Tree once. This takes O(n) because all elements are
traversed once. 

Encoded data is built by searching each character in the dictionary.
The efficiency of this is O(n).

##### Huffman Encoding Efficiency:
	O(n) + O(n log n) + O(n) + O(n) = O(n log n)

### Huffman Decoding:
The runtime of my Huffman decoding is done in O(n), and is iterated
once - search is done with my Character_Tuple class which are 
the elements in my Huffman Tree.

##### Huffman Decoding Efficiency:
	O(n)
