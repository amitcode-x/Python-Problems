# Wap to print only char at odd index position

s = input('Enter a string :')
for ip in range(len(s)):
    if ip%2!=0:
        print(s[ip])
