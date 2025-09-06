# wap to print all digit present in string

s = input('Enter a string :')
ns= ''
for char in s:
    if char.isdigit():
        ns +=char
print(ns)
