# Definition of the generator to produce even numbers.
def all_even():
  n = 0
  while True:
    yield n
    n += 2

my_gen = all_even()

# # Generate the first 10 even numbers.
for i in range(5):
  print(next(my_gen))

# # Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# # Now go back to generating more even numbers.
for i in range(20):
  print(next(my_gen))


# ---------------------------------------------------------------

def product(a, b):
  output = a * b
  return output

def factoral_generator():
  i = 1
  n = i
  while True:
    output = product(n, i)
    yield output
    i += 1
    n = output

# Test Block
my_generator = factoral_generator()
num = 5
for i in range(num):
  print(next(my_generator))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120