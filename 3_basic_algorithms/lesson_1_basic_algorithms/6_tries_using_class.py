# Tries Using a Class
'''
Just like most tree data structures, let's use classes to
build the Trie. Implement two functions for the Trie class
below. Implement add to add a word to the Trie.
Implement exists to return True if the word exist in the
trie and False if the word doesn't exist in the trie.
'''


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        # Adding 'word' to trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        # Check if word exists in trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()


# Add Words
for word in word_list:
    word_trie.add(word)


# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
