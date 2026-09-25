str=input("Enter alphanumeric values:")
digits=[]
for ch in str:
    if ch.isdigit():
        digits.append(int(ch))
print(digits)
print("Sum of digits:",sum(digits))