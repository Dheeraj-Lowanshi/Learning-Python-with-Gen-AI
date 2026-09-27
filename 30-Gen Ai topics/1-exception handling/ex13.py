import math

a=input("Enter first number: ")
b=input("Enter second number: ")
c=input("Enter power for exponent: ")

try:
    a=int(a)
    b=int(b)
    c=int(c)
    div=a/b
    print("division of",a,"and",b,"is",div)
    res=math.exp(c)
    print("Exponent of",c,"is",res)
except(ArithmeticError):
    print("Power is too large")
except(ValueError):  
    print("Please do not input non numeric data")
except(ZeroDivisionError):
    print("Please do not input 0 as denominator")

    
