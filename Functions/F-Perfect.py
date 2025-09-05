# wap to print Perfect num in give a range using function

def isPerfect(n):
    sum_div = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum_div += i
    else:
        if sum_div == n:
            return True
        else:
            return False


def PerfectNum(LL,UL):
    for n in range(LL,UL+1):
        if isPerfect(n):
            print(n)
PerfectNum(1,30)