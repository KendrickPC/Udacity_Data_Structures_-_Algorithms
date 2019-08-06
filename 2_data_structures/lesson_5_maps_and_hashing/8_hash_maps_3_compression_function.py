'''
Compression Function:

We now have a good hash function which will return unique values
for unique objects. But let's look at the values. These are huge.
We cannot create such large arrays. So we use another function
- compression function to compress these values so as to create
arrays of reasonable sizes.

A very simple, good, and effective compression function can be
mod len(array). The modulo operator % returns the remainder of
one number when divided by other.

So, if we have an array of size 10, we can be sure that modulo
of any number with 10 will be less than 10, allowing it to fit
into our bucket array.

Because of how modulo operator works, instead of creating a new
function, we can write the logic for compression function in our
get_hash_code() function itself.

Check out the Khan Academy tutorial below:
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-multiplication

(A * B * C) mod D = (A mod D * B mod D * C mod D) mod D
'''


class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.prime = 31
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        # compress hash_code
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets

            # compress coefficient
            current_coefficient *= self.prime
            current_coefficient = current_coefficient % num_buckets

        # one last compression before returning.
        return hash_code % num_buckets

    def size(self):
        return self.num_entries
