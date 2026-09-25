#function definition
def calculate(x,y):
    total=x+y
    diff=x-y
    return total,diff

#function call
a=int(input("Enter first int:"))
b=int(input("Enter second int:"))

c=calculate(a,b)
print("Sum is:",c[0])
print("Difference is:",c[1])