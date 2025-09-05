# Wap to print Armstrong number in a given range




def isArmstron(n):
    digit = str(n)
    l = len(digit)
    summ = 0
    for i in digit:
        summ +=int(i) **l
    else:
        if summ == n:
            return True
        else:
            return False
def Armstrong(LL,UL):
    for n in range(LL,UL+1):
        if isArmstron(n):
            print(n)
Armstrong(1,30)
