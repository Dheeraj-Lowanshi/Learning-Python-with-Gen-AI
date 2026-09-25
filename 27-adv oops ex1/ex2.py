class Emp:
    def __init__(self,age,name,sal):
        self.age=age
        self.name=name
        self.__sal=sal
    


e=Emp(25,"Ajay",45000)
print(e.age)
print(e.name)
print(e._Emp__sal)