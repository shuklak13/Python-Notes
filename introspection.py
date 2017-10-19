# callable(object)
    # returns True if object is callable (class or function), False if not
# dir(object)
    # returns the list of attributes of an object
# getattr(object, attr)
    # returns the value of object.attr
# setattr(object, attr, value)
    # sets the value of object.attr (and creates object.attr if it did not exist before)

def info(object):
    """Print all methods of an object"""
    methodList = [attr for attr in dir(object) 
        if callable(getattr(object, attr))]
    print("\n".join([method for method in methodList]))

listObject = []
info(listObject)


# isinstance(object, class)
    # returns True if object is an instance of class
# issubclass(class1, class2)
    # returns True if class1 is a subclass of class2

class Foo(object): pass

foo = Foo()

print(str(isinstance(foo, Foo)))    #True
print(str(isinstance(foo, object))) #True; an instance of subclass is an instance of a superclass
print(str(isinstance(Foo, Foo)))    #False; a class is not an instance of itself
print(str(isinstance(Foo, object))) #True; a class is an instance of its superclass
print(str(issubclass(Foo, Foo)))    #True; a class is a subclass of itself
print(str(issubclass(Foo, object))) #True


# eval(expression)
    # return the result of evaluating an expression in Python

from math import *
user_func = input("type a function: f(x) = ")
for x in range(1,10):
	print("x = ", x , "\t\tf(x) = ", eval(user_func))


# property()
    #