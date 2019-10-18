class PartyAnimal:
    x = 0
    def __init__ (self):
        print('I am constructed')

    def party(self):
        self.x =self.x + 1
        print("So far",self.x)
        
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an = 42
print('an contains' ,an)

print(type(an))
print(dir(an))


# "an" = PartyAnimal
# an.party() initializes PartyAnimal, so you get the printout "I am constructed"
# an.party() fires off "party", so you get "So far 1"
# an.party() fires off "party" again, so you get "So far 2"
# When an no longer equals PartyAnimal (it = 42) the template gets destructed (_del_) 
# and thrown away, so you get "I am destructed"


