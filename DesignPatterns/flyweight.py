class Circle(object):
    
    # the flyweight design pattern suppresses the internal dictionary
        # and instead uses a list, called `__slots__`
    # this dramatically increases memory efficiency
    __slots__ = ['diameter']

    def(self, radius):
        self.radius = radius

    # like a getter()
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


c = Circle(1.0)
print(str(c.radius()))
c.radius = 2.0
print(str(c.radius()))