class vehicle:
    def __init__ (self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
name = str(input("what vehicle:"))
maxspeed = int(input("maxspeed of vehicle"))
mileage = float(input("miles per hour of vehicle"))
ob = vehicle(name,maxspeed,mileage) 
print (ob.name)
print (ob.maxspeed) 
print (ob.mileage)
     