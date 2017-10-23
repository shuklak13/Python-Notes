# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://realpython.com/blog/python/instance-class-and-static-methods-demystified/#delicious-pizza-factories-with-classmethod

class A(object):
    # instance method   (traditionally use "self")
    def instance_foo(self):
        print("%s"%(self))

    #                   (traditionally use "cls")
    @classmethod
    def class_foo(cls):
        print("%s"%(cls))

    @staticmethod
    def static_foo():
        print("hi")

a=A()

# instance methods are called using an object
    # the first parameter refers to the object
# use when you want to reference an object instance
a.instance_foo() #<__main__.A object at 0x00000176F8DF2128>

# class methods can be called using the class or an object
    # the first parameter refers to the class
# use when you want to reference a class
A.class_foo()  #<class '__main__.A'>
a.class_foo()  #<class '__main__.A'>

# static methods can be called using the class or an object
    # no parameter refers to the class or object
# use when you want to group functions under a class's namespace
A.static_foo() #hi
a.static_foo() #hi