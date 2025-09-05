# Wap to print Disarium numbers in a given rangeDisarium numbers
        

def isDisarium(n):
    digit = str(n)
    summ = 0
    pos =1
    for i in digit:
        summ +=int(i) **pos
        pos+=1
    else:
        if summ == n:
            return True
        else:
            return False
def Disarium(LL,UL):
    for n in range(LL,UL+1):
        if isDisarium(n):
            print(n)
Disarium(1,100)