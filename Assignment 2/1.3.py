from turtle import width


class Rectangle:
    def __init__(self , length , width):
      self.length = length
      self.width = width
    def getLenght(self):
        return self.length 
    def setlength(self, length):
        self.length=length     
    def getwidth(self):
        return self.width
    def setwidth(self,width):
        self.width=width
    def Area(self):
        return self.length * self.width    
    def Perimeter(self):
        return (self.length + self.width) * 2 
    def Info(self):
        print(f"Area = {self.Area()} \n Perimeter = {self.Perimeter()}")
    

rect = Rectangle(1 , 1)
rect.Info()
           
