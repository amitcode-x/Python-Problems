# wap to print prime num in give a range using function



def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False

def PrimeNum(ll,ul):
    for n in range(ll,ul+1):
        if isPrime(n):
            print(n)

            
PrimeNum(1,30)
