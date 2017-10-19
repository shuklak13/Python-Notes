# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

# Only 1 instance

# initialized in a private, static variable
# retrieved through  public, static method, `getInstance()`

# When to use Singletons
#    when you need to hold some state information that changes over time
# When to use Static Classes
#    when you don't need to hold a "state", just a collection of functions
#       (for example, a Math class)

class Singleton:
    # a double-underscore, AKA a "dunderscore" creates a class-local reference
        # it does this by renaming the variable into "Singleton__Instance"
        # dunderscores 
    # This prevents subclasses from accidentally overwriting this reference
    class __Instance: