# Wap to print char only index 2 and 6

        
s = input('Enter a string :')
for ip in range(len(s)):
    if ip == 2 or ip ==6:
        print(s[ip])
