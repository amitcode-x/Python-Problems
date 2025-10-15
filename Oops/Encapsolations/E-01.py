class IPL:
    semis = 'this time our game'
    _finals = 'One more step away to trophy'
    __trophy = 'finally we made it'

    def heart(self):
        print('RCB has won heart but not trophy')
    def _display(self):
        print('protected display')
    def __happiness(self):
        print('no more heart winning only trophy')

RCB = IPL()
print(RCB.semis)
RCB.heart()
print(RCB._finals)
RCB._display()
print(RCB._IPL__trophy)
RCB._IPL__happiness()