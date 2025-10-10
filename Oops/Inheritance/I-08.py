class Vehicle:
    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def car_info(self):
        super().start()
        print('this is a car')

c = Car()
#c.start()
c.car_info()