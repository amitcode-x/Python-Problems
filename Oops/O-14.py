class Bank:
    bank_roi = 5
    @classmethod
    def modify_roi(cls):
        print(cls)
        cls.bank_roi=4
        print('modified')

amit=Bank()
sumit=Bank()
#Object method sirf  object se call hota hai class se nhi
Bank.modify_roi()
print(sumit.bank_roi)
print(amit.bank_roi)
print(Bank.bank_roi)
