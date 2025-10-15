class Emp:
    cname='psp'
    cloc='banglore'
    e_count=0
    def __init__(self,en,es,ej,ex):
        self.ename=en
        self.esal=es
        self.ejob=ej
        self.eexprence=ex
        Emp.e_count +=1
    def __del__(self):
        Emp.e_count -= 1
amit = Emp('amit',4500000000000,'developer',1)
sumit = Emp('amit',4500000000000,'developer',1)

print(sumit.e_count)

del amit

print(sumit.e_count)
  
  
 