

data1={"a":1,"b":2,"c":3}
data2={x:y*2 for x,y in data1.items() if y%2==0}

print(data2)