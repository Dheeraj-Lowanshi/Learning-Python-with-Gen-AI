check_even=lambda n:n%2==0
mylist=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(check_even,mylist))
print(result)