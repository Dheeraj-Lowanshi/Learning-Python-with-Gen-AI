str=input("Enter a string: ")
i=0
str=str.lower()
while i<len(str):
    if str[i] in "aeiou":
        print("String contains vowel")
        break
    i=i+1
else:
    print("String does not contain vowel")