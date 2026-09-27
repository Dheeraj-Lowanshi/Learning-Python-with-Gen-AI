
a=int(input("Enter numerator:"))
b=int(input("Enter denominator:"))


try:
    div=a/b
    print("Division of",a,"and",b,"is",div)
except (ZeroDivisionError):
    print("Denominator must be 0")
finally:
    print("Have a good day!")
