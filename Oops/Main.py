class Library:
    library_name = 'City Central Library'
    library_location = 'Downtown'
    fine_per_day = 2
    
    def __init__(self, user_name, user_id, borrowed_books=None):
        self.user_name = user_name
        self.user_id = user_id
        if borrowed_books is None:
            self.borrowed_books = {}
        else:
            self.borrowed_books = borrowed_books

    @staticmethod
    def get_int_input(prompt=''):
        try:
            value = int(input(prompt))
        except ValueError:
            print('Please enter a valid number')
            value = Library.get_int_input(prompt)
        return value

    def show_user_details(self):
        print(f'User Name: {self.user_name}')
        print(f'User ID: {self.user_id}')
        print('Borrowed Books:')
        if not self.borrowed_books:
            print('No books borrowed')
        else:
            for book, days in self.borrowed_books.items():
                print(f'Book: {book}, Days Borrowed: {days}')

    def borrow_book(self):
        book_name = input('Enter Book Name to Borrow: ')
        days = self.get_int_input('Enter number of days to borrow: ')
        if book_name in self.borrowed_books:
            print(f'You already borrowed "{book_name}"')
        else:
            self.borrowed_books[book_name] = days
            print(f'Book "{book_name}" borrowed for {days} days')

    def return_book(self):
        book_name = input('Enter Book Name to Return: ')
        if book_name in self.borrowed_books:
            days_borrowed = self.borrowed_books.pop(book_name)
            print(f'Book "{book_name}" returned')
            overdue_days = max(0, days_borrowed - 7)  # assuming 7 days free
            if overdue_days > 0:
                fine = overdue_days * Library.fine_per_day
                print(f'Late return! Fine: {fine} units')
            else:
                print('Returned on time. No fine!')
        else:
            print(f'Book "{book_name}" not found in your borrowed list')

    def extend_borrow_days(self):
        book_name = input('Enter Book Name to Extend: ')
        if book_name in self.borrowed_books:
            extra_days = self.get_int_input('Enter extra days: ')
            self.borrowed_books[book_name] += extra_days
            print(f'Borrow period for "{book_name}" extended by {extra_days} days')
        else:
            print(f'Book "{book_name}" not found')

    @classmethod
    def update_fine(cls):
        new_fine = cls.get_int_input('Enter new fine per day: ')
        cls.fine_per_day = new_fine
        print(f'Library fine per day updated to {cls.fine_per_day} units')
    def __del__(self):
        print(f'user {self.user_name} object is deleted')
    def __str__(self):
        pass
  
class Bank:
    bank_name='sbi'
    banck_branch= 'main branch'
    bank_roi = 5
    def _init__(self,ac,n,b):
        self.account=ac
        self.name=n
        self.balance=b
    def customer_details(self):
        print(f"Account Number: {self.account}")
        print(f"Customer Name: {self.name}")
        print(f"Account Balance: {self.balance}")
    def widthdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Withdrawn amount:{amount}")
            print(f"Remaining balance:{self.balance}")
        print("Thank you for banking with us!",self.balance)
         
        

# Users
alice = Library('Alice', 101)
bob = Library('Bob', 102)

# Example interactions
alice.show_user_details() 
alice.borrow_book()
alice.borrow_book()
alice.show_user_details()
alice.return_book()
alice.extend_borrow_days()
alice.show_user_details()
Library.update_fine()
