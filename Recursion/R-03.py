# WAP to find Sum of first n number using recursion.


def summ(n):
    if n==0 :
        return 0
    return n+summ(n-1)
print(summ(5))