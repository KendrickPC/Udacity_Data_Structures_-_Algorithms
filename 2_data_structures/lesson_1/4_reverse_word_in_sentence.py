# Code 

def word_flipper(our_string):
    split_string = our_string.split()
    for i in range(len(split_string)):
        split_string[i] = split_string[i][::-1]
    
    return " ".join(split_string)
        

print(word_flipper("testing function."))

# Test Cases

# print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")


