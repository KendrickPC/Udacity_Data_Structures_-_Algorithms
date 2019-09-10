# Request Routing in a Web Server With a Trie

I create a trie data structure conceived from a data tree.

First, I initialize the RouteTrie setting self.root to
a RouteTrieNode() class representing a route containing a children
dictionary. The routes for our children have been linked to my
RouteTrieNode class storing data there.

My RouteTrie class traverses my tree and returns the data. 

For my Router class, the algorithm is built upon the RouteTrie class.
If the url is not found, I set a default error message to be returned.

Now, my Trie class finds words, using autocomplete, and I have also
added an insert function as well.

### Time Complexity
For my insert function the time complexity is O(n).
My lookup route time complexity is O(log(n))

### Space Complexity
The efficiency of my space complexity is O(nm). 
'n' represents the number of paths and 'm' represents the size of letters
connecting to other tries.
