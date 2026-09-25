#function definition
def calculate(x,y):
    z=x+y
    return z

#function call
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("The sum of",x,"and",y,"is:",calculate(x,y))