'''
Hash Functions:

Simply put, hash functions are these really incredible magic
functions which can map data of any size to a fixed size data.
This fixed sized data is often called hash code or hash digest.

Let's create our own hash function to store strings.

'''


# def hash_function(string):
#   pass


'''
For a given string, say abcd, a very simple hash function can
be sum of corresponding ASCII values.

Note: you can use ord(character) to determine ASCII value of
a particular character e.g. ord('a') will return 97.
'''

# Example of a bad hash function.
'''
def hash_function(string):
    hash_code = 0
    for character in string:
        hash_code += ord(character)
    return hash_code

hash_code_1 = hash_function("abcd")
print(hash_code_1)
'''
# <<< 394
# There are 24 permutations of "abcd" that will return 394.


'''
Looks like our hash function is working fine.
But is this really a good hash function?

For starters, it will return the same value for abcd and bcda.
Do we want that? We can create 24 different permutations for the
string abcd and each will have the same value. We cannot put 24
values to one index.

Obviously, this makes it clear that our hash function must return
unique values for unique objects.

When two different inputs produce the same output, then we have
something called a collision. An ideal hash function must be
immune from producing collisions.

Let's think something else.

Can product help? We will again run in the same problem.

The honest answer is that we have differernt hash functions for
different types of keys. The hash function for integers will be
different from the hash function for strings, which again, will be
different for some object of a class that you created.

However, let's try to continue with our problem and try to come
up with a hash function for strings.
'''


'''
Hash Function for Strings:

For a string, say abcde, a very effective function is treating
this as number of prime number base p. Let's elaborate this
statement.

For a number, say 578, we can represent this number in base 10
number system as:

5 ∗ 10^2 + 7 ∗ 10^1 + 8 ∗ 10^0

Similarly, we can treat abcde as

𝑎∗𝑝^4 + 𝑏∗𝑝^3 + 𝑐∗𝑝^2 + 𝑑∗𝑝^1 + 𝑒∗𝑝^0

Here, we replace each character with its corresponding ASCII value.

A lot of research goes into figuring out good hash functions and
this hash function is one of the most popular functions used for
strings. We use prime numbers because they provide a good
distribution. The most common prime numbers used for this
function are 31 and 37.

Thus, using this algorithm, we can get a corresponding integer
value for each string key and store it in the array.

Note that the array used for this purpose is called a bucket
array. It is not a special array. We simply choose to give a
special name to arrays for this purpose. Each entry in this
bucket array is called a bucket and the index in which we store
a bucket is called bucket index.

Let's add these details to our class.
'''

class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        # Usually using 31 or 37.
        self.prime = 31
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.prime
            current_coefficient = current_coefficient

        return hash_code

hash_map = HashMap()
bucket_index = hash_map.get_bucket_index("abcd")
print(bucket_index)
# <<< 3077374

hash_map = HashMap()
bucket_index = hash_map.get_bucket_index("bcda")
print(bucket_index)
# <<< 2988994
















