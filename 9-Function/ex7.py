#function definition
def absolute(n):
    if n>0:
        return n
    else:
        return -n

#function call
a=int(input("Enter first number:"))
b=absolute(a)
print("Absolute of",a,"is",b)