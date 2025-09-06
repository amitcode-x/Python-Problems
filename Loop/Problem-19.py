# wap to print only special char

s = input('Enter a string: ')
for char in s:
    if not char.isdigit() and not char.isalpha():
        print(char)