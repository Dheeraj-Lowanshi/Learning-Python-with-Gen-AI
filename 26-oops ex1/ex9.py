import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        area = math.pi * math.pow(self.radius, 2)
        return area

    def cal_circumference(self):
        circumference = math.tau * self.radius
        return circumference
    


rad=int(input("Enter radius: "))
obj=Circle(rad)
area=obj.cal_area()
print("Area is",area)
circumference=obj.cal_circumference()
print("Circumference is",circumference)