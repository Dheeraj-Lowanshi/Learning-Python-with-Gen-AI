str=input("Enter a string: ")
i=0
ch=""
while i<len(str):
    ch=str[i]
    i=i+1
    if ch in "aeiouAEIOU":
        continue
    print(ch)
