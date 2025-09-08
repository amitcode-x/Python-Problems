# wap to print triangular numbers in a given range
def isTriangular(n):
    summ = 0
    i = 1
    while summ < n:
        summ += i
        if summ == n:
            return True
        i += 1
    else:
        return False


def TriangularNum(LL, UL):
    for n in range(LL, UL + 1):
        if isTriangular(n):
            print(n)


# Test
TriangularNum(1, 100)
