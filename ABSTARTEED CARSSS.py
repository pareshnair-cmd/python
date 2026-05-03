from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def feat (self,maxspeed):
        pass
class toyota(car):
    def feat (self,maxspeed):
        print ("Toyota goes",maxspeed,"km") 
    def type (self,type):
        print ("toyota",type)   
class mercedes(car):
    def feat (self,maxspeed):
        print ("mercedes goes",maxspeed,"km")
    def type (self,type):
        print ('mercedes',type)    
car1 = toyota()
car2 = mercedes()
car1.feat(1002)
car1.type("Hyundai")
car2.feat(1200)
car2.type("Benz")