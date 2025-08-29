# wap to replace every space in a string with by place (_)
s = input('Enter a string :')
ns=''
for ele in s:
    if ele == ' ':
        ns += '_'
    else:
        ns +=ele   
print(ns)