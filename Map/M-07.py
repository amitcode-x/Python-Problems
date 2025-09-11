# i/p = [11,22,30,13]
# o/p = [false,true,true,false]


def ip(l):
    return l%2==0
print(list(map(ip,[11,22,30,13])));