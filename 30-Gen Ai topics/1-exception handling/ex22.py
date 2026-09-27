

import os

try:
    a=int(input("Enter numerator:"))
    b=int(input("Enter denominator:"))
    div=a/b
    print("Division of",a,"and",b,"is",div)
    os._exit(0)   #success exit
except (ZeroDivisionError):
    print("Denominator must be 0")
finally:
    print("Have a good day!")
