# wap to print sunny numbers in a given range
def isSunny(n):
    x = n + 1
    root = int(x ** 0.5)
    if root * root == x:
        return True
    else:
        return False


def SunnyNum(LL, UL):
    for n in range(LL, UL + 1):
        if isSunny(n):
            print(n)


# Test
SunnyNum(1, 100)
