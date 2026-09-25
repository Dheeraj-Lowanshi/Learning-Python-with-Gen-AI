str=input("Enter a string: ")
i=0
while i<len(str):
    if str[i] in "aeiouAEIOU":
        print("String contains vowel")
        break
    i=i+1
else:
    print("String does not contain vowel")