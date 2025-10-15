class Rectangle:
    def __init__(self,h,w):
        self.height=h
        self.width=w
        self.area = h*w
    def __gt__(self,other):
        return self.area > other.area
R1= Rectangle(500,100)
R2= Rectangle(200,100)
print(R1>R2)