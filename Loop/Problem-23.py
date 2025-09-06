# wap to count space present in string

s = input('Enter a string: ')
count = 0
for char in s:
    if char == ' ':
        count +=1
print(count)
