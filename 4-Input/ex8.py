import math

radius = float(input("Enter radius: "))
area = math.pi * math.pow(radius, 2)
circum= math.tau * radius
print("Area of circle is",round(area,2)) 
print("Circumference of circle is",round(circum,2))