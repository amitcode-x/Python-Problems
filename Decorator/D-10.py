def timeDecorator(arg):
    def inner(ll,ul):
        import time
        it = time.time()
        arg(ll,ul)
        ft= time.time()
        print(ft)
    return inner

@timeDecorator
def primeNum(ll,ul):
    for n in range(ll,ul+1):
        if n>1:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
            else:
                print(n)

primeNum(1,100)