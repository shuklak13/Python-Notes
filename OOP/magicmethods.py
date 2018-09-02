# https://www.python-course.eu/python3_magic_methods.php

class Pet(object):
    """contains a pet name and species"""
    # __doc__: the docstring
    # __dict__: the object's parameter names and values as a dictionary

    # doggo = Pet("Arnold", "Dog")
    def __init__(self, name, species):
        """initialize a pet by name and species"""
        self.name = name
        self.species = species
    
    # doggo("King", "Dog")
    def __call__(self, name, species):
        """overwrite a pet's name and species"""
        self.name = name
        self.species = species
    
    # converts to string - for readability
    def __str__(self):
        return("%s is a %s" % (self.name, self.species))

    # converts to an unambiguous programmer representation - for logging and debugging
    def __repr__(self):
        return self.species + " " + self.name

    # dir(object) == object.__dir__
    # by default, returns a list of attributes
    # but can be overwritten to do whatever you want
    def __dir__(self):
        return self.__dict__

    # convert to int; __float__ also exists
    def __int__(self):
        return int(self.name)

    # called on `self + other`
    # __sub__, __mul__, and more exist
    def __add__(self, other):
        return Pet(self.name + other.name,
                    self.species + other.species)

    # called on `self += other`
    # __isub__, __imul__, and more exist
    def __iadd__(self, other):
        self.name = self.name + other.name
        self.species = self.species + other.species

     # called on `self < other`
    # __gt__, __le__, __ge__, __eq__, and __ne__ exist
    def __lt__(self, other):
        return self.species < other.species

