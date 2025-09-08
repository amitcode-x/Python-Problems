
# wap to print automorphic numbers in a given range
def isAutomorphic(n):
    sq = n * n
    dummy = n
    while dummy > 0:
        if dummy % 10 != sq % 10:
            return False
        dummy //= 10
        sq //= 10
    else:
        return True


def AutomorphicNum(LL, UL):
    for n in range(LL, UL + 1):
        if isAutomorphic(n):
            print(n)


# Test
AutomorphicNum(1, 500)
