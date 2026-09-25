def square(n):
    return n*n

mylist=[2,3,6,8,4]
res = map(square,mylist)
print(list(res))