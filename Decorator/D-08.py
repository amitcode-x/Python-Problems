def outer(arg):
    print('Outer is started')
    print(arg)
    def inner():
        print('Inner is started ')
        print(arg)
        arg()
        print('inner is ended')
    print('outer is ended')
    return inner

@outer
def hai():
    print('hai started')
    print('hai ended')

hai()

