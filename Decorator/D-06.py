def decorator(arg):
    def inner():
        print('Inner is started')
        print(arg)
        print ('inner is ended')
    return inner
@decorator
def decorated():
    pass
    
decorated()
