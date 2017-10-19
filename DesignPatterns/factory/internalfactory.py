#Only the factory can create instances of the generated classes

class Shape(object):
    @staticmethod
    def factory(type):
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert False, "Bad shape creation: " + type

    class Circle(Shape):
        def draw(self): print("Circle.draw")

    class Square(Shape):
        def draw(self): print("Square.draw")

types = [subclass.__name__ for subclass in Shape.__subclasses__()]
for t in types:
    shape = Shape.factory(t)
    shape.draw()