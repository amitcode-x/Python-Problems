
# Passing another functions address as a value to the argument





def outer(arg):
    print('first line of outer')
    print(arg)
    def inner():
        print('first line of inner')
        print(arg)
        arg()
        print('last line of inner')
    print('last line of outer')
    return inner
def hai():
    print('hai is started')
    print('hai is ended ')
res = outer(hai)
print(res)
res()
