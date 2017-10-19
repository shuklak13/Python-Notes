class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return("%s is a %s" % (self.name, self.species))

class Dog(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, "Dog")

class Cat(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, "Cat")


for subclass in Pet.__subclasses__():
    print(subclass.__name__ )