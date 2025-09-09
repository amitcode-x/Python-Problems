# WAP to calculate the power of a number (x^n) using recursion.

def power(x,n):
    if n==0 :
        return 1
    return x*power(x,n-1)
print(power(9,2))
