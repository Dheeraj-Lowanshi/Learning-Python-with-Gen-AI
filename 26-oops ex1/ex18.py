class Emp:
    x=10

    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal
    

    def display(self):
        self.x=self.age+10
        print("age:",self.age,"name:",self.name,"salary:",self.sal)
        print("x:",self.x)  

e=Emp(25,"Ajay",45000)
f=Emp(30,"Vijay",50000)
e.display()
f.display()
print(Emp.x)
