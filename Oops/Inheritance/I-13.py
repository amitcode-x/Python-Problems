
# --------------------------------------------------------Hybrid Inheritance---------------------------------------------------




#combination of multiple and multi level



class A:
    a = 100
    b = 300
    def m1(self):
        print('m1 of A')
class B():
    B = 400
    c = 999
    def __init__(self,m):
        self.m=m
    def m2(self):
        print('m2 of B')
class C(A):
    pass
class D(B):
    pass

class E(C,D):
    pass



print(E.mro()) #E-->C-->A-->D-->B-->Object