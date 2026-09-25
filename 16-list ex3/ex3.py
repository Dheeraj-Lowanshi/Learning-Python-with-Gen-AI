str=input("Enter alphanumeric values:")
digits=[]
for ch in str:
    if ch in "0123456789":
        digits.append(int(ch))
print(digits)
print("Sum of digits:",sum(digits))