# --------------------------------------------------------Hybrid Inheritance---------------------------------------------------


#combination of multiple and multi level And Hierarchical Inheritance


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
class D(B,C):
    pass

print(D.mro()) #D-->B-->C-->A-->Object