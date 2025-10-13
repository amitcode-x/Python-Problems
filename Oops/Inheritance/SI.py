# ------------------------------------------------------Single inheritance Example---------------------------------------------------------------------


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"This is a vehicle from {self.brand}")

class Car(Vehicle):
    def car_type(self):
        print("This is a Car")


c = Car("Toyota")
c.info()
c.car_type()