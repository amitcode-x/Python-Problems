


# --------------------------------------------------------Hirarchial Inheritance---------------------------------------------------



class A:
    a = 100
    b = 300
    def m1(self):
        print('m1 of A')
class B(A):
    B = 400
    c = 999
    def __init__(self,m):
        self.m=m
    def m2(self):
        print('m2 of B')
class C(A):
    pass



oc = C()
oc.m1()
print(C.mro()) #C-->A-->Object

ob = B(100)
ob.m1()
print(B.mro()) #B-->A-->Object


