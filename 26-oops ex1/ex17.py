class Emp:
    x=10

    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal
    

    def display(self):
        print("age:",self.age,"name:",self.name,"salary:",self.sal)
        print("x:",Emp.x)  

e=Emp(25,"Ajay",45000)
f=Emp(30,"Vijay",50000)
e.display()
f.display()
