# Building a Trie in Python
'''
Before we start, let's reiterate the key components of a Trie or Prefix
Tree. A trie is a tree-like data structure that stores a dynamic set of
strings. Tries are commonly used to facilitate operations like predictive
text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function, we need to create a working
trie for storing strings. We will create two classes:

    - A Trie class that contains the root node (empty string)
    - A TrieNode class that exposes the general functionality of the Trie,
      like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the TrieNode and Trie classes below!
'''

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.string = ""
        self.children = [None] * 26
        self.finalWord = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        node = TrieNode()
        node.string = node.string + char
        index = ord(char) - ord('a')
        if not (self.children[index]):
            self.children[index] = node
            print(node.string, end=" ")

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        rootNode = self.root
        for i in word:
            index = ord(i) - ord('a')
            if (rootNode.children[index] == None):
                rootNode.insert(i)
            rootNode = rootNode.children[index]
        rootNode.finalWord = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        rootNode = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if (rootNode.children[index] == None):
                return False
            rootNode = rootNode.children[index]
        return rootNode

# Finding Suffixes
'''
Now that we have a functioning Trie, we need to add the ability to list
suffixes to implement our autocomplete feature. To do that, we need to
implement a new function on the TrieNode object that will return all
complete word suffixes that exist below it in the trie. For example, if
our Trie contains the words ["fun", "function", "factory"] and we ask for
suffixes from the f node, we would expect to receive ["un", "unction",
"actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes
function below. (Hint: recurse down the trie, collecting suffixes as you
go.)
'''

class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.string = ""
        # Matching against 26 letters in the alphabet 
        self.children = [None] * 26
        self.finalWord = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        node = TrieNode()
        node.string = node.string + char
        index = ord(char) - ord('a')
        if not (self.children[index]):
            self.children[index] = node
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        temp_list = []
        for node in self.children:
            if node is not None:
                s = suffix + node.string
                if (node.finalWord):
                    temp_list.extend([s])
                    temp_list.extend(node.suffixes(s))
                else:
                    temp_list.extend(node.suffixes(s))
        return temp_list

# Testing it all out
'''
Run the following code to add some words to your trie and then use the
interactive search box to see what your code returns.
'''

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
