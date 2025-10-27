# List comprehension  syntax with one value and one for loop and one if consition
# syntax:

# variablename = [value forloop in consition]

# from the given tuple add only odd num into the list


T = (11,22,33,44,45,46,54,77,888,99,3,1,7,23,67)

L = [i for i in T if i%2==1]
print(L)