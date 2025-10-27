# value , forloop, if consition and else
# syntax :
# varname = {value if condition else  forloop }


l = [1,2,3,1,33,2,4,-99,-4,-3]

data = {i if i>0 else 0 for i in l }
L = [i if i>0 else 0 for i in l ]
print(data)
print(L)