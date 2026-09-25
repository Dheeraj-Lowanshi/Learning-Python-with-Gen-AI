from math import pi, pow, tau

radius = float(input("Enter radius: "))
area = pi * pow(radius, 2)
circum= tau * radius
print("Area of circle is",round(area,2)) 
print("Circumference of circle is",round(circum,2))
