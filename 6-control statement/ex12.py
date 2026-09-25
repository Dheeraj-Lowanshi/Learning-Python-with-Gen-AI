a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if(a>b):
    if(a>c):
        print("The largest number is {}".format(a))
    else:
        print("The largest number is {}".format(c))
else:
    if(b>c):
        print("The largest number is {}".format(b))
    else:
        print("The largest number is {}".format(c))
