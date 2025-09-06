# wap to count uppercase and lowercase latter

s = input('Enter a string: ')
upper = 0
lower = 0
for char in s:
    if char.isupper():
        upper +=1
        
    else:
        lower+=1
        
print(f" upper case is {upper} and Lower case is {lower} ")