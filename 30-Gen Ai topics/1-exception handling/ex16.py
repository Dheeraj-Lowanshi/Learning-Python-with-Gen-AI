

a=input("Enter first number: ")
b=input("Enter second number: ")

try:
    a=int(a)
    b=int(b)
    div=a/b
    print("division of",a,"and",b,"is",div)
except(ZeroDivisionError,ValueError)as ex:
    print("Some problem occurred:",ex) #print(ex.__str__())

    
