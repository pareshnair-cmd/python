class BMW:
    def __init__(self,fuel_type,maxspeed):
        self.fuel_type = fuel_type
        self.maxspeed = maxspeed
    def engine(self):
        print ("BMW uses", self.fuel_type,self.maxspeed)
class ferrari:
    def __init__(self,fuel_type,maxspeed):
        self.fuel_type = fuel_type
        self.maxspeed = maxspeed
    def engine(self):
        print ("Ferrari uses", self.fuel_type,self.maxspeed, )
obbmw = BMW("High octane petrol / diesel", "566km")
obferrari = ferrari("Pure petrol", "997km")
for car in (obbmw,obferrari):
    car.fuel_type
