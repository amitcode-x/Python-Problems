import time

# Original isPrime function
def isPrime(n):
    if n > 1:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

def PrimeNum(ll, ul):
    st = time.time()
    for n in range(ll, ul + 1):
        if isPrime(n):
            print(n, end=" ")
            print( )
    
    et = time.time()  # End timer
    print(f"Time taken: {et - st:.6} seconds")
PrimeNum(1, 30)
