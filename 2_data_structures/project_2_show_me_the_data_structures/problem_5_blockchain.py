# PEP8 Verified
# Blockchain
'''
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to
the other blocks in the chain. Each block contains a cryptographic hash
of the previous block, a timestamp, and transaction data. For our
blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when
the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a
blockchain implementation.

    https://en.wikipedia.org/wiki/Blockchain
    https://en.wikipedia.org/wiki/SHA-2
    https://en.wikipedia.org/wiki/Greenwich_Mean_Time
'''
# Python Hash Library Documentation
# https://docs.python.org/3/library/hashlib.html
import hashlib
# Python Datetime Library Documentation for GMT time.
# https://docs.python.org/3/library/datetime.html
import datetime as dt
'''
We do this for the information we want to store in the block
chain, such as transaction time, data, and information like the
previous chain.
'''
# The next main component is the block on the blockchain:
# The below is template code by Udacity, but I added a data
# object for the self.hash initialization process.
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    # The below is template code for calculating hash, but I 
    # added a data object to the hash_str encoding. 
    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


'''
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain,
which you will be doing by implementing it in a linked list.
All of this will help you build up to a simple but full
blockchain implementation!
'''


# Initializing Node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Initializing Block_Chain_Linked_list
class Block_Chain_Linked_List(object):
    def __init__(self, head=None):
        self.head = head
        self.previous_hash = self.head

    # Appending new data into hash with the function
    # below.
    def append(self, timestamp, data):
        if self.head is None:
            blockchain = Block(timestamp, data, self.previous_hash)
            self.head = Node(blockchain)
            self.previous_hash = blockchain.hash
            return

        node = self.head
        while node.next is not None:
            node = node.next
        blockchain = Block(timestamp, data, self.previous_hash)
        self.previous_hash = blockchain.hash
        node.next = Node(blockchain)


    def converting_list(self):
        hash_list = []
        node = self.head
        while node is not None:
            hash_list.append(node.value)
            node = node.next
        return hash_list


    def print_block(self, hash_list):
        for block_hash in hash_list:
            print("", block_hash.timestamp,
                  "\nData: ", block_hash.data,
                  "\nPrevious Hash: ", block_hash.previous_hash,
                  "\nCurrent Hash: ", block_hash.hash + "\n")


hash_list = Block_Chain_Linked_List()
hash_list.append(dt.datetime.now(), "first blockchain")
hash_list.append(dt.datetime.now(), "second blockchain")
hash_list.append(dt.datetime.now(), "third blockchain")
hash_list.append(dt.datetime.now(), "fourth blockchain")
hash_list.append(dt.datetime.now(), "fifth blockchain")
hash_list.print_block(hash_list.converting_list())
