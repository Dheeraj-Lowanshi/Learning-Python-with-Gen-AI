class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal


    def display(self):
        print("age:",self.age,"name:",self.name,"salary:",self.sal)
        del e.sal



e=Emp(25,"Ajay",45000)
e.display()
print(e.__dict__)
