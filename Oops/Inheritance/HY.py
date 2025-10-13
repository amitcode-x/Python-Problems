# -----------------------------------------------------------------Hybrid Inheritance Example-------------------------------------------------------------



class Person:
    def personal_info(self):
        print("This is a person")

class Employee(Person):
    def employee_info(self):
        print("This is an employee")

class Manager(Employee, Person):
    def manager_info(self):
        print("This is a manager")

m = Manager()
m.personal_info()
m.employee_info()
m.manager_info()