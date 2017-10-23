# nhttps://sourcemaking.com/design_patterns/singleton

# Basically, a Singleton is a global variable in class form

# Only 1 instance, initialized as a private, static variable in a class
# Accessible through public, static method
    # "static" = class-level (rather than instance-level)

# When to use Singletons
    # when you need centralized management of some data with global point-of-access
    # Examples: Loggers, Configs, Factories
# When to use Static Classes instead
    # when you don't need to hold data, just a collection of functions
        # in Python, classes are only a good solution if you need to hold data
        # otherwise, just use a module
    #  Example: Math

# How to use singletons?
    # Treat as a regular object you create - singleton functionaltiy is encapsulated
# reference_to_singleton = Singleton()
# reference_to_singleton.methodCalls()

################################################################################

def test_if_singleton(S):
    m1 = S()
    m2 = S()
    if(m1 is m2):
        print("Yep, this is a singleton")
    else:
        print("This ain't no singleton")

################################################################################

# Example: Singleton, a class containing an instance

class Singleton:

    class __Instance:
        """ a sample instance w/ only one param, arg"""
        def __init__(self, arg=None):
            self.val = arg
    
    instance = None     # create lazily to save space + time if never called

    def __init__(self, arg):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Instance(arg)
        else:
            Singleton.instance.val = __Instance(arg)


test_if_singleton(Singleton)

################################################################################

# Example: SingletonMetaclass, a metaclass that makes any class created from it into a singleton

class SingletonMetaclass(type):
    # recall that name, bases, and attrs are needed for `type()`
        # recall that types are the internal representation of a metaclass
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None    # create the instance lazily to save space+time

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class MySingleton(metaclass=SingletonMetaclass):
    pass

test_if_singleton(MySingleton)
