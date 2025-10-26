# Fibonacci series using generator in a range of N numbers
def FiboGen(fv,sv,n):
    i = 1
    while i <= n:
        i += 1
        yield fv
        fv,sv=sv,fv+sv

fgo = FiboGen(2,3,10)
for i in fgo:
    print(i)




