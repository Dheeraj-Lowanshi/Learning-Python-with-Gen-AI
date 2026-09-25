str=input("Enter a string: ")
for ch in str:
    if ch in "aeiouAEIOU":
        continue
    print(ch)