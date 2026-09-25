import math as m

radius = float(input("Enter radius: "))
area = m.pi * m.pow(radius, 2)
circum= m.tau * radius
print("Area of circle is",round(area,2)) 
print("Circumference of circle is",round(circum,2))
