class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.sal=sal

    def __str__(self):
        return f"Age:{self.age}, Name:{self.name}, Salary:{self.sal}"


a=[10,20,30]
b=(15,25,35)
c={"roll":101,"name":"sumit"}
print(a)
print(b)
print(c)
e=Emp(24,"Ravi",45000)
print(e)
