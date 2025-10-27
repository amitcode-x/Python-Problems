# value , forloop, if consition
# syntax :
# varname = {value forloop if condition}


l = [1,2,3,1,33,2,4]

data = {i for i in l if i %2==0}
print(data)