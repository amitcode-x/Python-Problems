
#create a cutome iterator to fetch fibonocci series of first N numbers
              
              
             
class FibonacciIterator:
    def __init__(self, n): 
        self.n = n     
        self.count = 0  
        self.a = 0      
        self.b = 1      
    def __iter__(self):
                
        self.count = 0   
        self.a, self.b = 0, 1  
        return self
                  
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration  

        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            next_val = self.a + self.b
            self.a, self.b = self.b, next_val
            self.count += 1
            return next_val



fib_io = FibonacciIterator(10)


fib_io.__iter__()


print(next(fib_io))  # 0
print(next(fib_io))  # 1
print(next(fib_io))  # 1
print(next(fib_io))  # 2
print(next(fib_io))  # 3
print(next(fib_io))  # 5
print(next(fib_io))  # 8
print(next(fib_io))  # 13
print(next(fib_io))  # 21
print(next(fib_io))  # 34
