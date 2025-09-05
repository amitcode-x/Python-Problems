# wap to print harshad num

def isharsad(n):
    digit = 0
    for i in str(n):
        digit += int(i)
    else:
        if digit !=0 and n%digit ==0:
            return True
        else:
            return False
def harshad(ll,ul):
    for n in range(ll,ul+1):
        if isharsad(n):
            print(n)
harshad(1,30)
