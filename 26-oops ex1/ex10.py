class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal
    def display(self):
        print("age:",self.age)
        print("name:",self.name)
        print("salary:",self.sal)



e=Emp(25,"Ajay",45000)
e.gender=("male")
print(e.__dict__)
f=Emp(30,"Vijay",50000)
print(f.__dict__)