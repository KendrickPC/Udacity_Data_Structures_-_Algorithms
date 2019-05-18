# Example function 1: return the sum of two numbers.
# def sum(a, b):
#     return a+b

# print(sum(3, 5))

my_list = [1, 2, 3, 4, 5]

def list_sort(my_list):
  my_list.sort()
  return len(my_list), my_list

print(list_sort(my_list))