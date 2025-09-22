# Nested Function returning integer as iutput


def outer(arg):
    print('first line of outer')
    print(arg)
    def inner():
        print('First line of inner')
        print(arg)
        print('last line of inner')
    inner()
    print('last line of outer')
    return 100
res=outer(23)
print(res)