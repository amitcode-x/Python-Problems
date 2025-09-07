# Wap to reverse of string without range function
L = eval(input('Enter a list :'))

for ip in range(len(L)):
    if ip %2==0:
        print(L[ip])