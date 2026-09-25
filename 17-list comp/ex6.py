#WAF which accepts a string and return a list containing all characters except vowle

def removevowle(str):
    mylist=[ch for ch in str if ch.lower() not in "aeiou"]
    return mylist


result=removevowle("I Live In India")
print(result)