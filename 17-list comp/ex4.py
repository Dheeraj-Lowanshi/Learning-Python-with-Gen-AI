#WAP to accept 5 integer from user, store them in a list. Finally display
#the list and sum of its memebers



mylist=[ int(ch) for ch in input("Enter a 5 int:").split() ]
print(mylist)
print("Sum of mylist:",sum(mylist))