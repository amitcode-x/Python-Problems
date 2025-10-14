from abc import ABC,abstractmethod
class Timetable(ABC):
    @abstractmethod
    def breakfast(self):
        pass
    @abstractmethod
    def lunch(self):
        pass
    @abstractmethod
    def dinner(self):
        pass


class Harshad(Timetable):
    def breakfast(self):
        print('Dosa')
    def lunch(self):
        print('daal chawal')
    def dinner(self):
        print('sabji roti')

H = Harshad()
H.breakfast()
H.lunch()
H.dinner()
