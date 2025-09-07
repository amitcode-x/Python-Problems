# Wap to reverse a list without using reverse function

L = eval(input('Enter a list :'))
rev = []
for i in L:
    
    rev = [i] + rev
print(rev)
