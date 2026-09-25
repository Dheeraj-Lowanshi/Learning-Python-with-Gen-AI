class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def __str__(self):
        return f"Age:{self.age}, Name:{self.name}"

class Emp(person):
    def __init__(self,age,name,id,sal):
        super().__init__(age,name)
        self.id=id
        self.sal=sal

    def __str__(self):

        return f"{super().__str__()}, ID:{self.id}, Salary:{self.sal}"


    

obj=Emp(24,"Nitin",101,50000)
print(obj)