#Create a list containing the words even
#or odd as per the numbers 1 to 10

mylist=["Even" if x%2==0 else "Odd" for x in range(1,11)]
print(mylist)