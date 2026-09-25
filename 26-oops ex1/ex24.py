class Emp:

    def __init__(self,age,name,sal,company):
        self.age=age
        self.name=name
        self.sal=sal
        Emp.company=company
    

    def display(self):
        self.x=self.age+10
        print("age:",self.age,"name:",self.name,"salary:",self.sal,"company:",Emp.company)

    def destroy(self):
        del Emp.company  

e=Emp(25,"Ajay",45000,"Google")
f=Emp(30,"Vijay",50000,"Google")
e.display()
f.display()
e.destroy()
print(Emp.__dict__)
