# wap to print EMIRP num in give a range using function



def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def rev(n):
    rev = 0
    while n >0:
        rem = n%10
        n//=10
        rev = rev*10+rem
    return rev
        
def EmirpNum(ll,ul):
    for n in range(ll,ul+1):
        r= rev(n)
        if isPrime(n) and r != n and isPrime(r):
            
            print(n)

EmirpNum(1,30)       
