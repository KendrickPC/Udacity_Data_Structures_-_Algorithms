# PEP8 Verified
# Huffman Coding
'''
A Huffman code is a type of optimal prefix code that is used
for compressing data. The Huffman encoding and decoding schema
is also lossless, meaning that when compressing the data to
make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond
to the relative frequency of each character for each character.
The Huffman code can be of any length and does not require a
prefix; therefore, this binary code can be visualized on a binary
tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm.
At the basic core, it is comprised of building a Huffman tree,
encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

    - Take a string and determine the relevant frequencies of
      the characters.
    - Build and sort a list of tuples from lowest to highest
      frequencies.
    - Build the Huffman Tree by assigning a binary code to each
      letter, using shorter codes for the more frequent letters.
      (This is the heart of the Huffman algorithm.)
    - Trim the Huffman Tree (remove the frequencies from the
      previously built tree).
    - Encode the text into its compressed form.
    - Decode the text from its compressed form.
    - create encoding, decoding, and sizing schemas.

For Example:
'''


import sys
from queue import PriorityQueue


# Initialize Character Tuple class
class Character_Tuple(object):
    def __init__(self, frequency, character):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None

    '''
    Less Than support of Character_Tuple
    Standard Operators as functions
    https://docs.python.org/2/library/operator.html
    '''
    def __lt__(self, other):
        return self.frequency < other.frequency


class Huffman_Coding(object):
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right

    '''
    Less Than support of Character_Tuple
    Standard Operators as functions
    https://docs.python.org/2/library/operator.html
    '''
    def __lt__(self, second_tuple):
        return second_tuple.frequency > self.frequency

    def __gt__(self, second_tuple):
        return second_tuple.frequency < self.frequency

    def __le__(self, second_tuple):
        return second_tuple.frequency >= self.frequency

    def __ge__(self, second_tuple):
        return second_tuple.frequency <= self.frequency


def huffman_encoding(data):
    # Base case data verification.
    if data is None or data is "":
        return data

    # Frequencies of each letter/character stored in
    # dictionary below
    frequency_map = dict()
    for character in data:
        if frequency_map.get(character) is not None:
            frequency_map[character] += 1
        else:
            frequency_map[character] = 1

    # Using the imported PriorityQueue library, sort the
    # characters in the frequency_map dictionary from lowest
    # to highest.
    priority_queue = PriorityQueue()
    for key in frequency_map:
        tuple = Character_Tuple(frequency_map[key], key)
        priority_queue.put(tuple)

    # Build the Huffman Tree until only 1 element is left
    # in the priority_queue
    while priority_queue.qsize() > 1:
        first_element = priority_queue.get()
        second_element = priority_queue.get()
        sum = first_element.frequency + second_element.frequency
        tuple = Character_Tuple(sum, '*')
        tuple.left = first_element
        tuple.right = second_element

        priority_queue.put(tuple)

    # Grab head of Huffman Tree, which is the last remaining
    # element of the priority_queue
    tree_head = priority_queue.get()

    print(tree_head)

    # Build Codes from codes_received
    codes = codes_received(tree_head, '', {})

    # Encode data
    encoded_data = ''
    for character in data:
        encoded_data += codes[character]

    return encoded_data, tree_head


def codes_received(node, prefix, codes):
    if not node.left and not node.right:
        codes[node.character] = prefix

    if node.left:
        codes_received(node.left, prefix + '0', codes)
    if node.right:
        codes_received(node.right, prefix + '1', codes)

    return codes


# Decode the text from its compressed form.
def huffman_decoding(data, tree):
    decode_data = ''
    node = tree
    for code in data:
        if code == '0':
            node = node.left
        elif code == '1':
            node = node.right

        if node.left is None and node.right is None:
            # reset node to tree
            decode_data += node.character
            node = tree

    return decode_data


if __name__ == "__main__":

    # Test Case 1:
    print("\nTest Case 1: ")
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))


    # Test Case 2:
    print("\nTest Case 2: ")

    a_great_sentence_testing_2 = "This is my second test case for the Huffman Coding Algorithm."
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence_testing_2)))
    print("The content of the data is: {}".format(a_great_sentence_testing_2))
    encoded_data, tree = huffman_encoding(a_great_sentence_testing_2)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))


    # Case 3
    print("\nTest Case 3: ")

    a_great_sentence_testing_3 = "我們現在看可不可以用中文還是只能用英文？"
    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence_testing_3)))
    print("The content of the data is: {}".format(a_great_sentence_testing_3))
    encoded_data, tree = huffman_encoding(a_great_sentence_testing_3)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
  


    # Edge Cases
    # Case 4
    print('\nEdge Case:')
    print('Case 4:')

    edge_case_testing_1 = "aaa"
    print("The size of the data is: {}".format(sys.getsizeof(edge_case_testing_1)))
    print("The content of the data is: {}".format(edge_case_testing_1))
    encoded_data, tree = huffman_encoding(edge_case_testing_1)
    # print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))

    # Case 5
    print("\nEdge Case:")
    print("Case 5:")
    edge_case_testing_2 = ""
    print("The size of the data is: {}".format(sys.getsizeof(edge_case_testing_2)))
    print("The content of the data is: {}".format(edge_case_testing_2))
    # print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))


'''
Resources:

    Huffman Visualization!
        https://people.ok.ubc.ca/ylucet/DS/Huffman.html

    Tree Generator:
        http://huffman.ooz.ie/

'''
