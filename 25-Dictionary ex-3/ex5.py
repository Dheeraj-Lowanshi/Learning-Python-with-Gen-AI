

str=input("Type a string:")

mydict={ch:str.count(ch)  for ch in str}

print(mydict)