from cmath import pi
from xml.etree.ElementTree import PI


class Circle:
    def __init__(self , raduis):
        self.raduis = raduis

    def getRaduis(self):
        return self.raduis
    
    def setRaduis(self , raduis):
        self.raduis = raduis
    
    def Area(self):
        return pow(self.raduis , 2) * pi

    def Circumfernce(self):
        return 2 * pi * self.raduis

    def Info(self):
        print(f"Raduis = {self.raduis} \n Area = {self.Area()} \n Circumfernce = {self.Circumfernce()}")


cir = Circle(1)
cir.Info()