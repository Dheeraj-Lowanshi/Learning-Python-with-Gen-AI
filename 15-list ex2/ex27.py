mylint=[]
print("Enter 5 unique int")
while True:
    num=int(input("Enter int:"))
    if num in mylint:
        print("Item already exist")
        continue
    mylint.append(num)
    if len(mylint)==5:
        break
print("5 unique values:",mylint)