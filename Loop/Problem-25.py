# Wap to print last 2 char in a string

s = input('Enter a string :')
length = len(s)
for i in range(length-2,length):
    print(s[i])