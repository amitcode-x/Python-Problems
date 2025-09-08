# wap to print neon numbers in a given range
def isNeon(n):
    sq = n * n
    summ = 0
    while sq > 0:
        rem = sq % 10
        summ += rem
        sq //= 10
    else:
        if summ == n:
            return True
        else:
            return False


def NeonNum(LL, UL):
    for n in range(LL, UL + 1):
        if isNeon(n):
            print(n)


# Test
NeonNum(1, 500)
