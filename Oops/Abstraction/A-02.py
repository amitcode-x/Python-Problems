from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def move(self):
        print('i can move')
    def speak(self):
        print('i can speak bow boww')
class  Snake(Animal):
    def move(self):
        print('i can move')
    def speak(self):
        print('Buss buss')
D=Dog()
D.speak()
D.move()
S=Snake()
S.speak()
S.move()
