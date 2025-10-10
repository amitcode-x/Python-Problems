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

OB=B(777)

print(B.mro()) #B-->A-->Object

print(B.__dict__)
print(OB.__dict__)