
# wap to print duck numbers in a given range
def isDuck(n):
    s = str(n)
 
    if s.startswith("0"):
        return False

    return "0" in s


def DuckNum(LL, UL):
    for n in range(LL, UL + 1):
        if isDuck(n):
            print(n)



DuckNum(1, 200)
