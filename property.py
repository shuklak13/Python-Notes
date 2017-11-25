

class Circle(object):
    def __init__(self):
        self.radius = None

    # like a getter()
    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            print("Impossible - radius must be positive")

    # like a destructor - called when the object is about to be deleted
    @radius.deleter
    def radius(self):
        print "So long, cruel world!"
        del self.radius


c = Circle()
c.radius = -1.0
c.radius = 1.0
print(str(c.radius))
c.radius = 2.0
print(str(c.radius))