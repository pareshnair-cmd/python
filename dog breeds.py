class dog:
    def __init__(self,name,breed,colour):
        self.name = name
        self.breed = breed
        self.colour = colour
ob1 = dog('Borossa','Poodle','white')
ob2 = dog('Ranger','Golden Retreiver','gold')
ob3 = dog('Packum','Husky','white and black') 
print (ob1.name,ob1.breed,ob1.colour)  
print (ob2.name,ob2.breed,ob2.colour)
print (ob3.name,ob3.breed,ob3.colour)
