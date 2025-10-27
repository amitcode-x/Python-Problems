#dictionary comprehension with zip function

a = [1,2,3]
#b ='hai'
b = 'hello'

dictval = {key : value for key,value in zip(a,b)}
print(dictval)