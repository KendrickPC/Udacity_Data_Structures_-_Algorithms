# -*- coding: utf-8 -*-

# Python Reverse Word
# https://www.geeksforgeeks.org/python-reverse-word-sentence/


def word_flipper(our_string):
    # Spliting the Sentence into list of words. 
    words = our_string.split(" ")

    # Reversing each word and creating 
    # a new list of words 
    # List Comprehension Technique 
    new_words = [word[::-1] for word in words]

    # Joining the new list of words 
    # to for a new Sentence 
    new_sentence = " ".join(new_words)
    return new_sentence

our_string_1 = "water"
our_string_2 = "This is an example"
our_string_3 = "This is one small step for ..."

print(word_flipper(our_string_1))
print(word_flipper(our_string_2))
print(word_flipper(our_string_3))


# Test Cases

# print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
# print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
