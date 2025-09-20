#  
class Bank:
    bank_name = 'sbi'
    bank_branch = 'marathahli'
    bank_roi =  5
    def __init__(self,cn,ac,b):
        print(self)
        self.cname= cn
        self.account = ac
        self.balance = b
amit = Bank('Amit chauhan',1234,100)
print("Customer Name:", amit.cname)
print("Account Number:", amit.account)
print("Balance:", amit.balance)