'''
In Python, the map concept appears as a built-in data type called
a dictionary. A dictionary contains key-value pairs. Dictionaries
might soon become your favorite data structure in Python — they're
extremely easy to use and useful.
Here's a sample of setting up a dictionary.
'''

udacity = {}
udacity['u'] = 7
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 1

print (udacity)
# <<< {'u': 7, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 1}

'''
In this case, the letters in "udacity" were each keys in our
dictionary, and the position of that letter in the string was
the value. Thus, I can do the following:
'''

print("\nValue of 't' is:")
print(udacity['t'])


'''
This statement is saying "go to the key labeled 't' and find
it's value, 6".

Dictionaries are wonderfully flexible—you can store a wide variety
of structures as values. You store another dictionary or a list:
'''

dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print (dictionary)
# <<< {'d': [1], 'i': [2, 5], 'c': [3], 't': [4], 'o': [6],
# <<< 'n': [7], 'a': [8], 'r': [9], 'y':[10]}


'''
Time to play with Python dictionaries! You're going to work on
a dictionary that stores cities by country and continent. One
is done for you - the city of Mountain View is in the USA,
which is in North America.

You need to add the cities listed below by modifying the structure.
Then, you should print out the values specified by looking them up
in the structure.

Cities to add: Bangalore (India, Asia) Atlanta (USA, North America)
               Cairo (Egypt, Africa) Shanghai (China, Asia)

locations = {'North America': {'USA': ['Mountain View']}}

Print the following (using "print").

A list of all cities in the USA in alphabetic order.
All cities in Asia, in alphabetic order, next to the name of the country.
In your output, label each answer with a number so it looks like this:

1
American City
American City

2
Asian City - Country
Asian City - Country
'''

# Code

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')

# TODO: Print a list of all cities in the USA in alphabetic order.
print("\n1")
united_states_sorted = (sorted(locations['North America']['USA']))
for city in united_states_sorted:
    print(city)

#print(locations['North America'])


# TODO: Print all cities in Asia, in alphabetic order,
# next to the name of the country
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']

print("\n2")
asian_cities = []
for countries, cities in locations['Asia'].items():
    cities_dash_country = cities[0] + " - " + countries
    asian_cities.append(cities_dash_country)

asia_sorted = sorted(asian_cities)
for city in asia_sorted:
    print(city)
