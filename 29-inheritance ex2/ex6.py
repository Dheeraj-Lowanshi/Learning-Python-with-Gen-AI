class A:
    def show(self):
        print("In show of class A....")

class B:
    def show(self):
        print("In show of class B....")

class C(B,A):
    pass
    

obj=C()
obj.show()