def Brother(arg):
    def inner():
        print('Brother has picked call')
        arg()
        print('Brother has Dis connected the call')
    return inner

@Brother
def sister():
    print('Sister is speaking start')
    print('sister is speacking stop')

sister()