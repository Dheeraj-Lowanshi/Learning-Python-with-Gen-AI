

a=input("Enter first number: ")
b=input("Enter second number: ")

try:
    a=int(a)
    b=int(b)
    div=a/b
    print("division of",a,"and",b,"is",div)
except(ZeroDivisionError,ValueError):
    print("Some problem occurred")

    
