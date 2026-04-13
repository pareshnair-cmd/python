class pokemon:
    def __init__(self,type,species):
        self.species = species
        self.type = type
pokemon1 = pokemon('Grass','Bulbasuar')    
pokemon2 = pokemon('Fire','Charizard') 
pokemon3 = pokemon('Water','Sqiurtle')
print (pokemon1.species)
print (pokemon2.species)
print (pokemon3.species)     
userchoice = str(input("Choose your pokemon: "))
if userchoice == "Bulbasaur" or "bulbasuar":
    print(pokemon1.species,",",pokemon1.type,"type")
if userchoice == "Charizard" or "charizard":
    print(pokemon2.species,",",pokemon2.type,"type")    
if userchoice == "Sqiurtle" or "sqiurtle":
    print(pokemon3.species,",",pokemon3.type,"type")

