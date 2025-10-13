# --------------------------------------------------------Hierarchical Inheritance Example---------------------------------------------------



class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r

rect = Rectangle()
circ = Circle()

print("Rectangle Area:", rect.area(10, 5))
print("Circle Area:", circ.area(7))
