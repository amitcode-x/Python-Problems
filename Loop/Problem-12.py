# Wap to print only alphabets(ignore digit and specials)


s = input('Enter a string :')
for ele in s:
    if ele.isalpha():
        print(ele)