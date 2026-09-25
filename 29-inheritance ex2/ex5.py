class A:
    def show(self):
        print("In show of class A")

class B:
    def show(self):
        print("In show of class B")

class C(A,B):
    pass
    

obj=C()
obj.show()
print(C.mro())
print(C.__mro__)