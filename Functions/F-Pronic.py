# wap to print pronic numbers in a given range
def isPronic(n):
    i = 1
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    else:
        return False


def PronicNum(LL, UL):
    for n in range(LL, UL + 1):
        if isPronic(n):
            print(n)


# Test
PronicNum(1, 200)
