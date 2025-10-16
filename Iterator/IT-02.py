# create a custom iterator to fetch range of values


class RangeIterator:
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
                res = self.i
                self.i +=self.up
                return res
            raise StopIteration


RIO =  RangeIterator(1,3)

RIO.__iter__()
print(RIO.__next__())
print(RIO.__next__())
print(RIO.__next__())
print(RIO.__next__())


for value in RIO:
    print(value)