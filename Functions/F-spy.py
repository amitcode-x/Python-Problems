
# Wap to print spy numbers in a given range 

def isSpy(n):
    summ = 0
    prod = 1
    dummy = n
    while dummy > 0:
        rem = dummy % 10
        summ += rem
        prod *= rem
        dummy //= 10
    else:
        return summ == prod


def SpyNum(LL, UL):
    for n in range(LL, UL + 1):
        if isSpy(n):
            print(n)

SpyNum(1, 500)
