def singleTon(clsAddress):
    l=[]
    def inner():
        if len(l) ==0:
            mco = clsAddress()
            l.append(mco)
        return l[0]
    return inner

@singleTon
class Multiplex():
    def __init__(self):
        self.tickets=300
    def booking(self,n):
        if n < self.tickets:
            self.tickets -= n
            print('ticktes got booked')
        else:
            print('ticktes are sold out')
        print('available ticktes are ',self.tickets)


krishna=Multiplex()
krishna.booking(200)
print(krishna)

ganesha=Multiplex()
ganesha.booking(200)
print(ganesha)
    