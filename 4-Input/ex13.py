import datetime

name=input("Enter your name: ")
age=int(input("Enter your age: "))

print("Hello",name)
print("You will be of 100 years in ", datetime.datetime.now().year + (100-age))