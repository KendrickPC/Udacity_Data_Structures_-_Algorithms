'''
Python Classes Review
Python Classes Overview

A class is a structure in object-oriented programming that allows functions
and related data to be grouped together.

In a Python class, an important concept is self, which is used to reference a
class instance's own variables and functions from within the class definition.
For example, if we had a class called Person and we wanted the class instances
to have a variable called age, we could store this information
by using self.age.

Also, if we wanted the class to have a function that would increment the age
of the person, we could define a function inside this class called
def birthday(self). In order to be a class function, birthday needs to include
the input variable self, as this is used for proper referencing within
the class.

Another important and commonly used function definition is the
class initializer, def __init__(self). 
The body of the initializer is where instance variable definitions should be
added, and the initializer initializes all the variables once an instance of
the class is created. Also, any input variables that a class needs to have,
such as a name for the person can be passed into initializer function.
'''

# self must be used when declaring a variable in an __init__ function so
# that each instance of the class has its own copy of that variable.

'''
Examples of Python Classes

Below is an example of a basic Person class. The class has two variables for
name and age, along with three functions for initializing the class,
incrementing the person’s age, and getting the person’s name.
'''

class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def get_name(self):
        return self.person_name

'''
Currently, we have one function for getting the class’s variable. This is
called an Accessor. The other function that the class has is actually
modifying one of the class’ variables, and that is called a Mutator.
We can make our Person older by calling birthday()
'''
bob = Person('Bob', 35)
print(bob.get_name())

bob.birthday()
print(bob.person_age)


ken = Person('Ken', 37)
print(ken.get_name())

ken.birthday()
print(ken.person_age)

