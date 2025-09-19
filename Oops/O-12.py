class Bank:
    bank_name='sbi'
    bank_branch='marathahlli'
    bank_roi=6
    def __init__(self,cn,ac,b):
        self.cname =cn
        self.acount=ac
        self.balance=b
    def Customer_details(self):
        print('customer name :',self.cname)
        print('customer acount no :',self.acount)
        print('customer name :',self.balance)
    def Withdraw(self):
        amount= int(input('Enter the amount :'))
        if amount <= self.balance:
            print('Withdraw is successful')
        else:
            print('Insufficient balance')
        print('Available balance is ',self.balance)
    def Deposite(self):
        amount=int(input('Enter the amount :'))
        self.balance +=amount
        print('Deposite successful')
        
amit = Bank('amit',1234,10000)
sumit = Bank('sumit',4,1500)
# method accessing by class
Bank.Customer_details(amit)
Bank.Customer_details(sumit)
#method accessing by object
amit.Customer_details()
sumit.Customer_details()
Bank.Withdraw(amit)
Bank.Deposite(amit)