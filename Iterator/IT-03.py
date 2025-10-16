
#create a cutome iterator to fetch cube of numbers present given range of value
class RangeCube:
    def __init__(self,sl,el,up=1):
        print("__init__")
        self.sl=sl
        self.el=el
        self.up = up
    def __iter__(self):
        print('__iter__')
        self.i=self.sl
        return self
    def __next__(self):
            print('__next__')
            if self.i<=self.el:
                res = self.i**3
                self.i +=self.up
                return res
            raise StopIteration


CIO =  RangeCube(1,3)

CIO.__iter__()
print(CIO.__next__())
print(CIO.__next__())
print(CIO.__next__())
print(CIO.__next__())

for value in CIO:
    print(value)