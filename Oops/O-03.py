#accessing generic properties by using class
#syntax:   className.classVariablename

class Bank:
    # ---- Class Variables ----
    bank_name = "State Bank of India"
    bank_branch = "Marathahalli, Bangalore"
    bank_roi = 5   # Rate of Interest

# ---- Objects ----
amit = Bank()
sumit = Bank()



print(Bank.bank_name)