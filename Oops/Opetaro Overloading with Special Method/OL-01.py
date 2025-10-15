class Book:
    def __init__(self,bn,bp,ba):
        self.bname=bn
        self.bprice=bp
        self.bauthor=ba
    def __add__(self,other):
        return self.bprice +other.bprice
    def __sub__(self,other):
        return self.bprice-other.bprice
    def __mul__(self,intvalue):
        return self.bprice*intvalue
    def __truediv__(self,intvalue):
        return self.bprice/intvalue



python = Book('python',10000,'Gudio Van Rossum')
django = Book('django',20000,'Harshad')
print(python+django)
print(django-python)
print(python*2)
print(python/2)