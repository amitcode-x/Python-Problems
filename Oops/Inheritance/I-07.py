class Bank_v1:
    bank_name = 'sbi'
    bank_branch = 'marathahlli'
    bank_roi = 5
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.caccount=ca
        self.cbalance=cb
    def customer_details(self):
        print(f'name of customer is {self.cname}')
        print(f'account of customer is {self.caccount}')
        print(f'balance of customer is {self.cbalance}')
    @staticmethod
    def get_int_value():
        iv = int(input())
        return iv
    def withdraw(self):
        print('Enter the withdraw amounts :')
        amount = self.get_int_value()
        if amount <= self.cbalance:
            self.cbalance -=amount
            print('withdraw is successful')
        else:
            print('insufficient balance')
        print('avaliable balance is ',self.cbalance)

        
    @classmethod
    def bank_details(cls):
        print(f'name of bank is {cls.bank_name}')
        print(f'branch of bank is {cls.bank_branch}')
        print(f'roi of bank is {cls.bank_roi}')

    @classmethod
    def modify_roi(cls):
        print('Enter the new Roi ')
        nroi = cls.get_int_value()
        cls.bank_roi = nroi
        print('roi is changed')
         
          
class Bank_v2(Bank_v1):     
    bank_branch='banglore'        
    bank_ifsc=123456            
    
    def __init__(self,cn,ca,cb,cp,cm):  
        super().__init__(cn,ca,cb)  
        self.cpin=cp  
        self.cmobile=cm        
    def customer_details(self):
        super().customer_details()
        print(f'mobile num of customer {self.cmobile}')
    def withdraw(self): 
        print('Enter the pin ') 
        pin = self.get_int_value() 
        if pin == self.cpin: 
            print('PIN verified successfully!')
            super().withdraw()
        else:
            print('❌ Incorrect PIN! Transaction cancelled.')
    def deposite(self):
        print('Enter the deposite amount')
        amount = self.get_int_value()
        self.cbalance += amount
        print('Deposite is successful')
    