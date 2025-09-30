class Bank:
    bank_name='sbi'
    bank_branch = 'marathahalli'
    bank_roi = 5
    def __init__(self,cn,ac,b):
        self.cname=cn
        self.account=ac
        self.balance=b
    @staticmethod
    def get_int_value():
        intval = int(input())
        return intval
    def customer_details(self):
        print(f'customer name is {self.cname}')
        print(f'customer acount no {self.account}')
        print(f'customer balance {self.balance}')
    def withdraw(self):
        print('Enter Amount: ')
        amount=self.get_int_value()
        self.balance -=amount
        if amount <=self.balance:
            print('withdraw sucesfull')
        else:
            print('Insufficient balance')
        print('available balance is',self.balance)
    def deposit(self):
        print('Enter Amount: ')
        amount= self.get_int_value()
        self.balance += amount
        print('deposit is successful')
    @classmethod
    def modify_roi(cls):
        print('Enter new roi: ')
        new_roi= cls.get_int_value()
        cls.bank_roi=new_roi
        print('roi is modified')
                    
                      
                
            
                         

amit=Bank('amit',3467,10000)
sumit= Bank('Sumit',456,1500)

#amit.customer_details()
amit.withdraw()
amit.deposit()
amit.modify_roi()