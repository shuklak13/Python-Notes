# https://stackoverflow.com/questions/1261875/python-nonlocal-statement


# default - use the local-most scope
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)
# inner: 2
# outer: 1
# global: 0

# nonlocal - use the outer scope
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)
# inner: 2
# outer: 2
# global: 0

# global - use the global scope
x = 0
def outer():
    x = 1
    def inner():
        global x
        x = 2
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)
# inner: 2
# outer: 1
# global: 2