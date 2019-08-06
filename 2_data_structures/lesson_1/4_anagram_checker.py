# Code

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: Write your solution here
    if len(str1) != len(str2):
    	return False
    else:
    	clean_str_1 = str1.replace(" ", "").lower()
    	clean_str_2 = str2.replace(" ", "").lower()
    	if sorted(clean_str_1) == sorted(clean_str_2):
    		return True
    	else:
    		return False
    
    # pass

# print(anagram_checker('racecar', 'racECar'))
# print(anagram_checker('racecar', 'racecarb'))
# print(anagram_checker('raceken', 'raceben'))

# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")