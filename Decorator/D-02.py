# Returning inner functions address from outer functions space to main space



def outer(arg):
    print('First line of outer ')
    print(arg)
    def inner():
        print('First line of inner')
        print(arg)
        print('last line of inner')
    print('last line of outer')
    return inner
res = outer(23)
print('*'* 30)
print(res)
res()
