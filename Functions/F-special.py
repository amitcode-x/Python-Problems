
# Wap to print special numbers in a given range

def isSpecial(n):
    dummy = n
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        fact = 1
        for i in range(1,rem+1):
            fact = fact*i
        summ +=fact
    else:
        if summ == n:
            return True
        else:
            return False


def SpecialNum(LL,UL):
    for n in range(LL,UL+1):
        if isSpecial(n):
            print(n)
SpecialNum(1,1000)
    