#modifying generic properties by using object
#syntax:   objectName.classVariablename = newvalue

class Bank:
    # ---- Class Variables ----
    bank_name = "State Bank of India"
    bank_branch = "Marathahalli, Bangalore"
    bank_roi = 5   # Rate of Interest

# ---- Objects ----
amit = Bank()
sumit = Bank()

#if we modify generic properties by using object then it modifie in that object only

amit.bank_roi = 6

print(sumit.bank_roi)
print(amit.bank_roi)