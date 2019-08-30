# PEP* Verified
# Finding the Square Root of an Integer
'''
Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because
sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
'''


def sqrt(number):
    # Handling negative numbers / user input value errors
    # and edge cases.
    if number < 0:
        return ValueError('Math Domain Error')
    # Handling base case scenarios.
    elif (number == 0 or number == 1):
        return number

    start = 0
    end = number

    # Running while loop as long as the start number is less than
    # the end number.
    while start <= end:
        # Integer division.
        average = (start + end) // 2

        if average * average == number:
            return average

        elif average * average < number:
            start = average + 1
            result = average

        else:
            end = average - 1

    return result


# Given Test Cases:
print("\nGiven Test Cases:")
print ("Pass" if (3 == sqrt(9)) else "Fail")
print ("Pass" if (0 == sqrt(0)) else "Fail")
print ("Pass" if (4 == sqrt(16)) else "Fail")
print ("Pass" if (1 == sqrt(1)) else "Fail")
print ("Pass" if (5 == sqrt(27)) else "Fail")

# Edge Test Cases:
print("\nEdge Case Testing:")
print(sqrt(-9))
# <<< Math Domain Error
print(sqrt(0))
# <<< 0
print(sqrt(1))
# <<< 1

# Testing large test cases.
print(sqrt(999999999999999999999999999999999999999))
# <<< an answer is returned quickly.
