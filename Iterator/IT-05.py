# bysir fiboIterator






class FeboIterator():
    def __init__(self,fv,sv,n):
        self.fv = fv
        self.sv = sv
        self.n = n

    def __iter__(self):
        self.i = 1
        return self
    def __next__(self):
        if self.i<=self.n:
            self.i+=1
            res= self.fv
            self.fv,self.sv= self.sv,self.fv+self.n
            return res
        raise StopIteration
FIO = FeboIterator(20,22,10)
for i in FIO:
    print(i)
    
