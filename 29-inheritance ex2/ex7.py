class A:
    def show(self):
        print("In show of class A....")

class B(A):
    def show(self):
        print("In show of class B....")

class C(A):
    def show(self):
        print("In show of class C....")

class D(B,C):
    pass
    

obj=D()
obj.show()