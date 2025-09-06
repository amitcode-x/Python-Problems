# wap to print only special char

  



s = input('Enter a string: ')
count = 0
for char in s:
    if not char.isdigit() and not char.isalpha():
        count +=1
print(count)
