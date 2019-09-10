# Problem 5

The objective of this problem is to build a Trie in python. First, I
create a working Trie for storing strings. Then I create a Trie class
containing the root node (empty string). The second class I create is
a TrieNode that exposes the general functionality of the Trie - inserting
a word or finding the node which represents a prefix.

With a functioning Trie complete, I add the ability to list suffixes to
implement the autocomplete features. This is achieved by implementation of 
a new function on the TrieNode object returning all complete word suffixes
that exist below the Trie.

For my TrieNode class, I initialize the string node with ""
For the children, I match it against 26 letters of the English alphabet.
my finalWord variable is set to False.

For insertion, I add a child node in the Trie. 

For the suffixes, I use recursion collecting suffixes for all complete
words below this point. I create a temporary list.

### Time Complexity
Time complexity for my algorithm is O(nm). 'n' represents the depth of
my trie and 'm' represents the length of each word.

### Space Complexity
For a worst case scenario, if we use a word with no matching characters,
this would require a node for each letter. This basically makes my space
complexity O(n), again making 'n' the depth of my Trie in my temp_list.
