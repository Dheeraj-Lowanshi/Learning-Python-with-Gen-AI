a=input("Enter first number: ")
b=input("Enter second number: ")

a=int(a)
b=int(b)

try:
    div=a/b
    print("division of",a,"and",b,"is",div)
except(ZeroDivisionError):
    print("Please do not input 0 as denominator")
else:
    print("Yay! You got it right") 