class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal

e=Emp(25,"Ajay",45000)
print("age:",e.age,"name:",e.name,"salary:",e.sal)

f=Emp(30,"Vijay",50000)
print("age:",f.age,"name:",f.name,"salary:",f.sal)