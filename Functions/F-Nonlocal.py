# Nonlocal

def outer():
    a =10
    print('inside OUTER ',a)
    def inner():
        nonlocal a
        print('inside inner',a)
        a +=10
        print('inside inner after modification',a)
    inner()
    print('inside OUTER after inner call',a)
outer()

