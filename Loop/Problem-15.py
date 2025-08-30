# wap to print every second char in a string

       
s = input('Enter a string: ')
count = 0
for ele in range(1,len(s),2):
    print(s[ele])