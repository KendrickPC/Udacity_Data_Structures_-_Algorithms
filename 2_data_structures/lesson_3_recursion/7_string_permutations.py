'''
String Permutations:

Problem Statement
Given an input string, return all permutations of the
string in an array.

Example 1:
string = 'ab'
output = ['ab', 'ba']

Example 2:
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
'''


def permutations(string):
    return return_permutations(string, 0)

def return_permutations(string, index):
    # Base Case
    if index >= len(string):
        return [""]

    small_output = return_permutations(string, index + 1)
    output = list()
    current_char = string[index]
    '''
    Iteration over each permutation string received and
    place the current character between indices of the
    string.
    '''
    for permutation in small_output:
        for index in range(len(small_output[0]) + 1):
            new_permutation = permutation[0: index] + current_char + permutation[index:]
            output.append(new_permutation)
    return output


# Test Case
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# Test 1
string = 'a'
solution = ['a']
test_case = [string, solution]
test_function(test_case)

# Test 2
string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

# Test 3
string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)


# Test 4
string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)

# <<< Pass
# <<< Pass
# <<< Pass
# <<< Pass
