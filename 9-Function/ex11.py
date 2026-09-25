#function definition
def calculate(x,y):
    total=x+y
    diff=x-y
    return total,diff

#function call
a=int(input("Enter first int:"))
b=int(input("Enter second int:"))

c,d=calculate(a,b)
print("Sum is:",c)
print("Difference is:",d)