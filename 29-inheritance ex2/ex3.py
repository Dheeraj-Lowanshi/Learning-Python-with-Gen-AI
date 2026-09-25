class Polygon:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def __str__(self):
        return f"dim1:{self.dim1},dim2:{self.dim2}"

class Rectangle(Polygon):
    def area(self):
        return f"Area of rect:{self.dim1*self.dim2}"

class Triangle(Polygon):
    def area(self):
        return f"Area of triangle:{0.5*self.dim1*self.dim2}"

r=Rectangle(10,20)
t=Triangle(5,7)
print("Rectangle dimensions:",r)
print("Area of rect:",r.area())
print("Triangle dimensions:",t)
print("Area of triangle:",t.area())