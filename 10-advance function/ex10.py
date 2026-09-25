


def findlargest(*args):
    max=0
    for s in args:
        if len(s) > max:
            max=len(s)
    return max

result=findlargest("Hi","Welcome","Hello")
print(result)