ch=input("Enter a character: ")
if "A" <= ch <= "Z":
    print("Capital letter")
elif "a" <= ch <= "z":
    print("Small letter")
elif "0" <= ch <= "9":
    print("Digit")
else:
    print("Special character")