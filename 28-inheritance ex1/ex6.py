import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def area(self):
        return 2*super().area()+2*math.pi*self.radius*self.height

    def volume(self):
        return super().area()*self.height


obj = Cylinder(5,10)
print("Area of Cylinder:", obj.area())
print("Volume of Cylinder:", obj.volume())
print("Area of circular part of Cylinder:", Circle.area(obj))