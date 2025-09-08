
# wap to print duck numbers in a given range
def isDuck(n):
    dummy = n


    if n == 0:
        return False
    while dummy >= 10:  
        dummy //= 10
    if dummy == 0:      
        return False


    dummy = n
    while dummy > 0:
        rem = dummy % 10
        if rem == 0:
            return True
        dummy //= 10

    return False


def DuckNum(LL, UL):
    for n in range(LL, UL + 1):
        if isDuck(n):
            print(n)

DuckNum(1, 200)
