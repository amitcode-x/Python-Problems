# wap to print evil numbers in a given range
def isEvil(n):
    ones = bin(n).count("1")
    if ones % 2 == 0:
        return True
    else:
        return False


def EvilNum(LL, UL):
    for n in range(LL, UL + 1):
        if isEvil(n):
            print(n)


# Test
EvilNum(1, 50)
