# wap to print magic numbers in a given range
def digitSum(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n //= 10
    return summ

def isMagic(n):
    dummy = n
    while dummy > 9:
        dummy = digitSum(dummy)
    else:
        return dummy == 1

def MagicNum(LL, UL):
    for n in range(LL, UL + 1):
        if isMagic(n):
            print(n)

# Test
MagicNum(1, 200)
