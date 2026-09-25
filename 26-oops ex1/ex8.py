import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        self.area=math.pi * math.pow(self.radius, 2)

    def cal_circumferance(self):
        self.circumference = math.tau * self.radius

    def display(self):
        print("Area is", self.area)
        print("Circumference is", self.circumference)


rad=int(input("Enter radius: "))
obj=Circle(rad)
obj.cal_area()
obj.cal_circumference()
obj.display()