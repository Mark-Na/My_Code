class Pet:
    allowed = ['cat', 'dog','fish','rat']
    def __init__(self,name,species):
        if species not in Pet.allowed: #can also use self instead of Pet
            raise ValueError(f"You can't have a {species} as a pet")
        self.name = name
        self.species = species
    
    def set_species(self,species):
        if species not in Pet.allowed: #can also use self instead of Pet
            raise ValueError(f"You can't have a {species} as a pet")
        self.species = species
cat = Pet("Blue","cat")
dog = Pet("Wyatt","dog")
#tiger = Pet("Tony","tiger")
Pet.allowed.append("pig")

# can only access class variables by doing name of class.classvar