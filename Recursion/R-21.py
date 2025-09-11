
# flatten list
# input  
# output ; [11,22,33,90,34,24,89]
# '''
L = [[11,22,33],90,[[34,24],89]]
def flatten(L):
    FL = []
    for ele in L:
        if isinstance(ele,int):
            FL.append(ele)
        else:
            FL.extend(flatten(ele))
    return FL
print(flatten(L))
