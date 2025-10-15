class Trainer:
    def __init__(self,tn,ts,tx):
        print('__init__ is called')
        self.tname=tn
        self.tsubject=ts
        self.texprence=tx
    def __str__(self):
        print('__str__ is called')
        return str(self.texprence)
    def __del__(self):
        print('__del__is called')

Harshad= Trainer('shaik harshad vali','python',6)
Parnay= Trainer('Parnay','python 2',4)
print(Harshad)
Harshad = None