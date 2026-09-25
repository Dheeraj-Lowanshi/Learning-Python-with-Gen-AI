import math
def cal_area(radius, pi=3.14):
    print("Area is", pi * math.pow(radius, 2))

radius=int(input("Enter radius: "))
cal_area(radius)