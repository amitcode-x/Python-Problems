# wap to print uppercase and lowercase latter



s = input('Enter a string: ')
upper = ' '
lower = ' '
for char in s:
    if char.isupper():
        upper +=char
        
    else:
        lower+=char
        
print(upper,lower)