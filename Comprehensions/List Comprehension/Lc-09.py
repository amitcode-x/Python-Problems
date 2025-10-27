# Value for loop and we r having multiple if consitions

# syntax:

# variablename = [value for loop if condition1 if consition2]

# normal approch
L = [1, 4, 6, -3, 10, 5, 8]
LL =[]
for i in L:
    if i >0 and i>5:
        LL.append(i)
print(LL)

# List comprehension approach


LL=[1,2,3,-88,100,-99,55,66,5]

L = [i for i in LL if i>0 if i >5 ]
print(L)