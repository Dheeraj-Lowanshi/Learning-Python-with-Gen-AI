class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal


    def display(self):
        print("age:",self.age,"name:",self.name,"salary:",self.sal)
        print("gender:",self.gender)



e=Emp(25,"Ajay",45000)
e.__dict__["gender"]="male"
f=Emp(30,"Jyoti",50000)
f.__dict__["gender"]="female"
f.__dict__["role"]="SDE-2"

e.display()
f.display()