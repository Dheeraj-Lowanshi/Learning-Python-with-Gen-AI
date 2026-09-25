age=int(input("Enter your age: "))
print("Your age is {}".format(age))

print("Kid") if age < 13 else print("Teenager") if age < 20 else print("Adult")