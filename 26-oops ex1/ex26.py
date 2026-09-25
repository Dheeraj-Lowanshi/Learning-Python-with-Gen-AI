class Emp:
    raise_amount=0.0

    @classmethod
    def set_raise_amount(cls,percent):
        cls.raise_amount=percent

    def __init__(self,nme,age,sal):
        self.name=nme
        self.age=age
        self.sal=sal

    def increase_sal(self):
        self.sal=self.sal+(self.sal*Emp.raise_amount/100)

    def display(self):
        print("name:",self.name,"age:",self.age,"salary:",self.sal)

e1=Emp("amit",22,50000)
e2=Emp("sumit",24,40000)
print("Before increment sa")
e1.display()
e2.display()

percent=float(input("Enter the raise amount:"))

Emp.set_raise_amount(percent)
e1.increase_sal()
e2.increase_sal()

print("After increment sa")
e1.display()
e2.display()