#WAP to accept 5 integer from user, store them in a list. Finally display
#the list and sum of its memebers


str=input("Enter a 5 int:")
mylist=[ int(ch) for ch in str.split() ]
print(mylist)
print("Sum of mylist:",sum(mylist))