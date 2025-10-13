
# --------------------------------------------------------Multilevel Inheritance Example---------------------------------------------------



class Vehicle:
    def show(self):
        print("This is a vehicle")

class Car(Vehicle):
    def fuel_type1(self):
        print("This car uses petrol or diesel")

class ElectricCar(Car):
    def fuel_type2(self):
        print("This car uses electricity")

ec = ElectricCar()
ec.show()
ec.fuel_type1()
ec.fuel_type2()