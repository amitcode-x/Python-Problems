# List comprehension syntax with one value one forloop and multiple if condition

# syntax:

# variablename = [value forloop if condition1 and if condition2]



T = (11,22,33,44,45,46,54,77,888,99,3,1,7,23,67)

L = [i for i in T if i%2==1 and i > 50]
print(L)
