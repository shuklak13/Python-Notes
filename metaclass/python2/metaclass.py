# How to make a class use a metaclass?
    # Add a __metaclass__ attribute to your class definition
# How to make all classes in a module uses a metaclass?
    # Add a __metaclass__ attribute in your module
# If neither of the above are done,
    # Python will use type() to create the class    (normal case)
class Baz(object):
  __metaclass__ = A_Metaclass
# What to put in the __metaclass__ attribute?
    # anything that creates a class
# What creates a class?
    # `type`, a subclass of `type()`, or a function that returns a `type()`