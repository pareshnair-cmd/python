import math
class circle:    
    def __init__ (self,radius):
        self.radius = radius
    def area(self): 
        areaofcircle = math.pi * self.radius * self.radius
        print (areaofcircle)
ob = circle(5) 
ob.area()       