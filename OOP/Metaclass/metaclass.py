# https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
# 2nd answer from top is the better one

# traditional class creation
class Foo(object):
    bar = True
    def echo_foo(self):
        print("foo")

# class creation via `type`
    # Class = type( 'ClassName',
    #               (superclasses),
    #               {'class': 'fields'}
    #           )
def echo_bar(self):
    print("bar")
Bar = type( 'Bar',
            (Foo),
            {'bar': True, 'echo_bar': echo_bar}
        )

# How can `type()` be used to create classes?
# Because `type` is a Metaclass!
    # In fact, `type` is the object internally used to create classes!
        # `type()` is a C-level function

# just like an objects are instances of classes, created when you call a class
    # MyObject = MyClass()
# classes are instances of metaclasses, created when you call a metaclass
    # MyClass = MetaClass()