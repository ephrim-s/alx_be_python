import math

class Shape:
    def area(self):
        raise NotImplementedError(NotImplementedError)


class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    

    def area(self):
        return self.lenght * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2