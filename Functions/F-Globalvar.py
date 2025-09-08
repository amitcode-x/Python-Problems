
# global


a = 10
def display():
    global a
    print('Inside function',a)
    a+=20
    print(a)
display()
print('in main space',a)