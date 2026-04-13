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
if userchoice == "Bulbasuar" or userchoice == "bulbasuar":
    print(pokemon1.species,",",pokemon1.type,"type")
elif userchoice == "Charizard" or userchoice == "charizard":
    print(pokemon2.species,",",pokemon2.type,"type")    
elif userchoice == "Sqiurtle" or userchoice == "sqiurtle":
    print(pokemon3.species,",",pokemon3.type,"type")

