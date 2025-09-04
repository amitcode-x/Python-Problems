# wap to print even num in give a range using function



def isEven(n):
    if n%2==0:
        return True
    else:
        return False

def evenNum(ll,ul):
    for i in range(ll,ul+1):
        if isEven(i):
            print(i)

evenNum(2,30)