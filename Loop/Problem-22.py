# wap to count how many digit present in string

s = input('Enter a string :')
count = 0
for char in s:
    if char.isdigit():
        count+=1
print(count)