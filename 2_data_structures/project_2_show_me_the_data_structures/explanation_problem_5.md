# Blockchain tracking

##### Algorithm Explanation:
I use a linked list to hash the data.
Each specific Block() stores a timestamp, data,
the previous_hash and current hash value.

My objective is to grab the data, append it to a variable, and 
calculate the hash value for that data.

With my Block_Chain_Linked_List class, I set my head to None. 
With my head set to None, the previous hash value for my head 
will return None.

Using my append() function, my code adds a new block my hash_list,
assigning hash values to previous hash values in my hash_list by 
way of linked lists. I append five values for testing.  

##### Efficiency:
My time complexity is O(n) where n represents the number of blocks
in the linked list.

My space complexity is O(n) - appending new hash values to my 
hash_list. The variable "n" represents the size of my hash_list. 
