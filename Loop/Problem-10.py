# Wap to print how many times a is appers in string


s = input('Enter a string: ')
count = 0
for ele in s:
    if ele == 'a':
        count +=1
print(count)