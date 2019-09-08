# Request Routing in a Web Server With a Trie

I create a trie data structured derived from a data tree.

First, I initialize the RouteTrie setting self.root to 
a RouteTrieNode() class.



It is similar to problem 5, except for the edge cases, like "root handler", and working with a hierarchy of web pages instead of strings. This problem is focused on the development of the of a trie a data structure derived from a tree, suited for a good ratio between time and space complexity.

Time and Space complexity
For the trie, time complexity of searching and inserting from a trie depends on the length of the path n that’s being searched for, inserted, making the runtime of these operations O(n). Looking into the space complexity of a trie, the worst case, would be when we have a path (or paths), with no common folders between them, hence having, a node for each path block (path between forward slashes). Resulting in a space complexity of
O(n).


In this we have to take the path and split the using '/' as separator and keep each word as a key. So, after the insertion into the trie we will lookup for the path if its found we have to display about handler and if it is not found we have to display not found handler as the path doesnt exit over here.

Time complexity:O(n) for the insertion into the trie and also the lookup Space complexity: O(nm) where is 'n' number of path components and 'm' is size of the words(which points to other tries)


Explanation
Router Trie implementation:

class RouteTrieNode: Represents a single route, has a children dictionary which has the child routes mapped to another RouteTrieNode, and has a data property to store the route's data.
class RouteTrie: Uses RouteTrieNode to create a tree structure. Inserts routes by breaking each route from /. Finds and returns the route's data by traversing the tree.
class Router: Build on top of RouteTrie, sets the router using RouteTrie, and a default error for when a route data is not found.
Design
Trie class can be used to insert and find words for autocomplete.

Big O
Route insert => O(n) Route lookup => O(log(n))

The time complexity of the code is O(n) where n is the number of paths in the url
Space complexity is O(n) where n is the number of paths in the url, as we pass the paths as an array.